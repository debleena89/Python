





struct adc_buf vsupply_adc_buf;
struct adc_buf vservos_adc_buf;

int mode;
static int time_since_last_mega128;
static int time_since_last_ppm;
int radio_ok, mega128_ok, radio_really_lost;

static const int failsafe[] = {0, 0, 0, 0, 0, 0, 0, 0, 0};

static int ppm_cpt, last_ppm_cpt;






static void to_autopilot_from_last_radio (void) {
  int i;
  for(i = 0; i < RADIO_CTL_NB; i++)
     to_mega128.channels[i] = last_radio[i];
  to_mega128.status = (radio_ok ? _BV(STATUS_RADIO_OK) : 0);
  to_mega128.status |= (radio_really_lost ? _BV(RADIO_REALLY_LOST) : 0);
  if (last_radio_contains_avg_channels) {
    to_mega128.status |= _BV(AVERAGED_CHANNELS_SENT);
    last_radio_contains_avg_channels = FALSE;
  }
  to_mega128.ppm_cpt = last_ppm_cpt;
  to_mega128.vsupply = VoltageOfAdc(vsupply_adc_buf.sum/AV_NB_SAMPLE) * 10;
  to_mega128.vsupply = 0;
}

void send_data_to_autopilot_task(void)
{
   if ( !SpiIsSelected() && spi_was_interrupted )
   {
      spi_was_interrupted = FALSE;
      to_autopilot_from_last_radio();
      spi_reset();
   }
}

int main( void )
{
  uart_init_tx();
  uart_print_string("FBW Booting $Id: main.c,v 1.1 2006/06/15 09:27:07 casse Exp $\n");

  adc_init();
  adc_buf_channel(3, &vsupply_adc_buf);
  adc_buf_channel(6, &vservos_adc_buf);
  timer_init();
  servo_init();
  ppm_init();
  spi_init();

  while( 1 )
  {
    test_ppm_task();
    check_mega128_values_task();
    send_data_to_autopilot_task();
    check_failsafe_task();
    if(timer_periodic())
    {
      static int _1Hz;
      static int _20Hz;
      _1Hz++;
      _20Hz++;
      if (_1Hz >= 60)
      {
	_1Hz = 0;
	last_ppm_cpt = ppm_cpt;
	ppm_cpt = 0;
      }
      if (_20Hz >= 3)
      {
	_20Hz = 0;
	servo_transmit();

      }
      if (time_since_last_mega128 < STALLED_TIME)
	time_since_last_mega128++;
      if (time_since_last_ppm < REALLY_STALLED_TIME)
	time_since_last_ppm++;
    }
  }
  return 0;
}
void test_ppm_task(void)
{
    if( ppm_valid )
    {
      ppm_valid = FALSE;
      ppm_cpt++;
      radio_ok = TRUE;
      radio_really_lost = FALSE;
      time_since_last_ppm = 0;
      last_radio_from_ppm();
      if (last_radio_contains_avg_channels)
      {
	mode = MODE_OF_PPRZ(last_radio[RADIO_MODE]);
      }
      if (mode == MODE_MANUAL)
      {
	servo_set(last_radio);
      }
    }
    else if (mode == MODE_MANUAL && radio_really_lost)
    {
      mode = MODE_AUTO;
    }
    if (time_since_last_ppm >= STALLED_TIME)
    {
      radio_ok = FALSE;
    }
    if (time_since_last_ppm >= REALLY_STALLED_TIME)
    {
      radio_really_lost = TRUE;
    }
}
void check_failsafe_task(void)
{
    if ((mode == MODE_MANUAL && !radio_ok) ||
	(mode == MODE_AUTO && !mega128_ok))
    {
      servo_set(failsafe);
    }
}
void check_mega128_values_task(void)
{
     if ( !SpiIsSelected() && spi_was_interrupted )
     {
      if (mega128_receive_valid)
      {
	time_since_last_mega128 = 0;
	mega128_ok = TRUE;
	if (mode == MODE_AUTO)
	  servo_set(from_mega128.channels);
      }
     }
    if (time_since_last_mega128 == STALLED_TIME) {
      mega128_ok = FALSE;
    }
}
