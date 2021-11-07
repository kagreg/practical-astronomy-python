#!/usr/bin/python3

import argparse
import json
from dateutil.parser import parse
import lib.pa_datetime as PA_DT
import cli_lib.pa_cli_datetime as PA_CLI_DT
import cli_lib.pa_cli_coordinates as PA_CLI_CO

def main():
	parser = argparse.ArgumentParser(description='Practical Astronomy CLI.')

	# Add argument groups
	actions_datetime_group = parser.add_argument_group(title="Actions - Date/Time")
	actions_coordinates_group = parser.add_argument_group(title="Actions - Coordinates")
	inputs_group = parser.add_argument_group(title="Inputs (used by Actions)")
	inputs_tz_group = parser.add_argument_group(title="Inputs (time zone management)")

	# Inputs
	inputs_group.add_argument("--az_deg", type=float, help="Azimuth - degrees.")
	inputs_group.add_argument("--az_min", type=float, help="Azimuth - minutes.")
	inputs_group.add_argument("--az_sec", type=float, help="Azimuth - seconds.")
	inputs_group.add_argument("--alt_deg", type=float, help="Altitude - degrees.")
	inputs_group.add_argument("--alt_min", type=float, help="Altitude - minutes.")
	inputs_group.add_argument("--alt_sec", type=float, help="Altitude - seconds.")
	inputs_group.add_argument("--civil_date", type=str, help="Civil date.  Input format: 'mm/dd/yyyy'")
	inputs_group.add_argument("--civil_time", type=str, help="Civil time.  Input format:  'hh:mm:ss'")
	inputs_group.add_argument("--decimal_degrees", type=float, help="Decimal degrees")
	inputs_group.add_argument("--decl_deg", type=float, help="Declination - degrees")
	inputs_group.add_argument("--decl_min", type=float, help="Declination - minutes")
	inputs_group.add_argument("--decl_sec", type=float, help="Declination - seconds")
	inputs_group.add_argument("--decl_lat1", type=str, help="Declination latitude, first object. Input format: 'deg:min:sec', e.g., '-8:13:30'")
	inputs_group.add_argument("--decl_lat2", type=str, help="Declination latitude, second object. Input format: 'deg:min:sec', e.g., '-16:41:11'")
	inputs_group.add_argument("--degrees", type=float, help="Degrees")
	inputs_group.add_argument("--decimal_hours", type=float, help="Decimal hours.  Input format: floating point number, e.g., 18.52416667")
	inputs_group.add_argument("--ecl_lat_deg", type=float, help="Ecliptic latitude - degrees")
	inputs_group.add_argument("--ecl_lat_min", type=float, help="Ecliptic latitude - minutes")
	inputs_group.add_argument("--ecl_lat_sec", type=float, help="Ecliptic latitude - seconds")
	inputs_group.add_argument("--ecl_long_deg", type=float, help="Ecliptic longitude - degrees")
	inputs_group.add_argument("--ecl_long_min", type=float, help="Ecliptic longitude - minutes")
	inputs_group.add_argument("--ecl_long_sec", type=float, help="Ecliptic longitude - seconds")
	inputs_group.add_argument("--epoch1", type=str, help="Epoch 1.  Input format: 'mm/dd/yyyy', e.g. '1/0.923/1950'.  Day can be fractional.")
	inputs_group.add_argument("--epoch2", type=str, help="Epoch 2.  Input format: 'mm/dd/yyyy', e.g. '6/1/1979'.  Day can be fractional.")
	inputs_group.add_argument("--gal_lat_deg", type=float, help="Galactic latitude - degrees")
	inputs_group.add_argument("--gal_lat_min", type=float, help="Galactic latitude - minutes")
	inputs_group.add_argument("--gal_lat_sec", type=float, help="Galactic latitude - seconds")
	inputs_group.add_argument("--gal_long_deg", type=float, help="Galactic longitude - degrees")
	inputs_group.add_argument("--gal_long_min", type=float, help="Galactic longitude - minutes")
	inputs_group.add_argument("--gal_long_sec", type=float, help="Galactic longitude - seconds")
	inputs_group.add_argument("--greenwich_date", type=str, help="Greenwich date.  Input format: 'mm/dd/yyyy'.  Fractional day is allowed, e.g., '6/19.75/2009'")
	inputs_group.add_argument("--geo_lat", type=float, help="Geographical latitude.  Input format: (+/-)##.##, e.g., -64.00")
	inputs_group.add_argument("--geo_long", type=float, help="Geographical longitude.  Input format: (+/-)##.##, e.g., -64.00")
	inputs_group.add_argument("--gst", type=str, help="Greenwich sidereal time.  Input format: 'hh:mm:ss'")
	inputs_group.add_argument("--ha_hr", type=float, help="Hour angle - hours.")
	inputs_group.add_argument("--ha_min", type=float, help="Hour angle - minutes.")
	inputs_group.add_argument("--ha_sec", type=float, help="Hour angle - seconds.")
	inputs_group.add_argument("--h_or_d", type=str, help="Use hours ('H') or degrees ('D')")
	inputs_group.add_argument("--lst", type=str, help="Local sidereal time.  Input format: 'hh:mm:ss'")
	inputs_group.add_argument("--jd", type=float, help="Julian date.  Input format: floating point number, e.g., 2455002.25")
	inputs_group.add_argument("--minutes", type=float, help="Minutes")
	inputs_group.add_argument("--ra_hr", type=float, help="Right ascension - hours.")
	inputs_group.add_argument("--ra_min", type=float, help="Right ascension - minutes.")
	inputs_group.add_argument("--ra_sec", type=float, help="Right ascension - seconds.")
	inputs_group.add_argument("--ra_long1", type=str, help="Right ascension longitude, first object. Input format: 'hh(or)deg:min:sec', e.g., '5:13:31.7'")
	inputs_group.add_argument("--ra_long2", type=str, help="Right ascension longitude, second object. Input format: 'hh(or)deg:min:sec', e.g., '6:44:13.4'")
	inputs_group.add_argument("--seconds", type=float, help="Seconds")
	inputs_group.add_argument("--ut", type=str, help="Universal time.  Input format:  'hh:mm:ss'")
	inputs_group.add_argument("--v_sh_deg", type=float, help="Vertical shift degrees.")
	inputs_group.add_argument("--year", type=int, help="Calendar year, e.g. 2019.")
	
	# Inputs (time zone management)
	inputs_tz_group.add_argument('--daylight_savings_time', dest='is_daylight_savings', action='store_true', help="Observe daylight savings time.")
	inputs_tz_group.add_argument('--standard_time', dest='is_daylight_savings', action='store_false', help="Observe standard time (default)")
	inputs_tz_group.set_defaults(is_daylight_savings=False)
	inputs_tz_group.add_argument("--zone_correction", type=int, help="Offset, in hours, for time zone correction.")

	# Actions - Date/Time
	actions_datetime_group.add_argument("--doe", action='store_true', help="Calculate date of Easter, for a given year.")
	actions_datetime_group.add_argument("--cd_to_dn", action='store_true', help="Convert civil date to day number.")
	actions_datetime_group.add_argument("--gd_to_jd", action='store_true', help="Convert Greenwich date to Julian date.")
	actions_datetime_group.add_argument("--jd_to_gd", action='store_true', help="Convert Julian date to Greenwich date.")
	actions_datetime_group.add_argument("--ct_to_dh", action='store_true', help="Convert civil time to decimal hours.")
	actions_datetime_group.add_argument("--dh_to_ct", action='store_true', help="Convert decimal hours to civil time.")
	actions_datetime_group.add_argument("--lct_to_ut", action='store_true', help="Convert local civil time to universal time.")
	actions_datetime_group.add_argument("--ut_to_lct", action='store_true', help="Convert universal time to local civil time.")
	actions_datetime_group.add_argument("--ut_to_gst", action='store_true', help="Convert universal time to Greenwich sidereal time.")
	actions_datetime_group.add_argument("--gst_to_ut", action='store_true', help="Convert Greenwich sidereal time to universal time.")
	actions_datetime_group.add_argument("--gst_to_lst", action='store_true', help="Convert Greenwich sidereal time to local sidereal time.")
	actions_datetime_group.add_argument("--lst_to_gst", action='store_true', help="Convert local sidereal time to Greenwich sidereal time.")

	# Actions - Coordinates
	actions_coordinates_group.add_argument("--a_to_dd", action='store_true', help="Convert angle to decimal degrees.")
	actions_coordinates_group.add_argument("--dd_to_a", action='store_true', help="Convert decimal degrees to angle.")
	actions_coordinates_group.add_argument("--ec_to_hc", action='store_true', help="Convert equatorial coordinates to horizontal coordinates.")
	actions_coordinates_group.add_argument("--ecl_c_to_equa_c", action='store_true', help="Convert ecliptic coordinates to equatorial coordinates.")
	actions_coordinates_group.add_argument("--equa_c_to_ecl_c", action='store_true', help="Convert equatorial coordinates to ecliptic coordinates.")
	actions_coordinates_group.add_argument("--equa_c_to_gal_c", action='store_true', help="Convert equatorial coordinates to galactic coordinates.")
	actions_coordinates_group.add_argument("--gal_c_to_equa_c", action='store_true', help="Convert galactic coordinates to equatorial coordinates.")
	actions_coordinates_group.add_argument("--hc_to_ec", action='store_true', help="Convert horizontal coordinates to equatorial coordinates.")
	actions_coordinates_group.add_argument("--mean_obliq_ecliptic", action='store_true', help="Calculate mean obliquity of the ecliptic.")
	actions_coordinates_group.add_argument("--ang_b_two_obj", action="store_true", help="Calculate angle between two objects.")
	actions_coordinates_group.add_argument("--rise_and_set", action="store_true", help="Calculate rise and set times.")
	actions_coordinates_group.add_argument("--precession", action="store_true", help="Calculate correction for precession.")
	actions_coordinates_group.add_argument("--nutation", action="store_true", help="Calculate nutation.")

	args=parser.parse_args()

	datetime_cl = PA_CLI_DT.CliDateTime(args)
	datetime_cl.eval_datetime()

	coordinates_cl = PA_CLI_CO.CliCoordinates(args)
	coordinates_cl.eval_coordinates()

if __name__ == "__main__":
    main()
