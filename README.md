# practical-astronomy-python

Algorithms from "[Practical Astronomy with your Calculator or Spreadsheet](https://www.amazon.com/Practical-Astronomy-your-Calculator-Spreadsheet/dp/1108436072)" by Peter Duffett-Smith, implemented in Python 3.  API documentation is published [here](https://jfcarr-astronomy.github.io/practical-astronomy-python/).

If you're interested in this topic, please buy the book!  It provides far more detail and context.

## CLI

Work is started on a command-line interface, but only the date/time functions are implemented, so far.  Results are formatted as JSON.

Invoke as `./pa-cli.py -h` to see all of the options:

```
$ ./pa-cli.py -h

usage: pa-cli.py [-h] [--az_deg AZ_DEG] [--az_min AZ_MIN] [--az_sec AZ_SEC] [--alt_deg ALT_DEG] [--alt_min ALT_MIN] [--alt_sec ALT_SEC] [--civil_date CIVIL_DATE] [--civil_time CIVIL_TIME] [--decimal_degrees DECIMAL_DEGREES]
                 [--decl_deg DECL_DEG] [--decl_min DECL_MIN] [--decl_sec DECL_SEC] [--degrees DEGREES] [--decimal_hours DECIMAL_HOURS] [--greenwich_date GREENWICH_DATE] [--geo_lat GEO_LAT] [--geo_long GEO_LONG] [--gst GST]
                 [--ha_hr HA_HR] [--ha_min HA_MIN] [--ha_sec HA_SEC] [--lst LST] [--jd JD] [--minutes MINUTES] [--seconds SECONDS] [--ut UT] [--year YEAR] [--daylight_savings_time] [--standard_time] [--zone_correction ZONE_CORRECTION]
                 [--doe] [--cd_to_dn] [--gd_to_jd] [--jd_to_gd] [--ct_to_dh] [--dh_to_ct] [--lct_to_ut] [--ut_to_lct] [--ut_to_gst] [--gst_to_ut] [--gst_to_lst] [--lst_to_gst] [--a_to_dd] [--dd_to_a] [--ec_to_hc] [--hc_to_ec]
                 [--mean_obliq_ecliptic]

Practical Astronomy CLI.

optional arguments:
  -h, --help            show this help message and exit

Actions - Date/Time:
  --doe                 Calculate date of Easter, for a given year.
  --cd_to_dn            Convert civil date to day number.
  --gd_to_jd            Convert Greenwich date to Julian date.
  --jd_to_gd            Convert Julian date to Greenwich date.
  --ct_to_dh            Convert civil time to decimal hours.
  --dh_to_ct            Convert decimal hours to civil time.
  --lct_to_ut           Convert local civil time to universal time.
  --ut_to_lct           Convert universal time to local civil time.
  --ut_to_gst           Convert universal time to Greenwich sidereal time.
  --gst_to_ut           Convert Greenwich sidereal time to universal time.
  --gst_to_lst          Convert Greenwich sidereal time to local sidereal time.
  --lst_to_gst          Convert local sidereal time to Greenwich sidereal time.

Actions - Coordinates:
  --a_to_dd             Convert angle to decimal degrees.
  --dd_to_a             Convert decimal degrees to angle.
  --ec_to_hc            Convert equatorial coordinates to horizontal coordinates.
  --hc_to_ec            Convert horizontal coordinates to equatorial coordinates.
  --mean_obliq_ecliptic
                        Calculate mean obliquity of the ecliptic.

Inputs (used by Actions):
  --az_deg AZ_DEG       Azimuth - degrees.
  --az_min AZ_MIN       Azimuth - minutes.
  --az_sec AZ_SEC       Azimuth - seconds.
  --alt_deg ALT_DEG     Altitude - degrees.
  --alt_min ALT_MIN     Altitude - minutes.
  --alt_sec ALT_SEC     Altitude - seconds.
  --civil_date CIVIL_DATE
                        Civil date. Input format: 'mm/dd/yyyy'
  --civil_time CIVIL_TIME
                        Civil time. Input format: 'hh:mm:ss'
  --decimal_degrees DECIMAL_DEGREES
                        Decimal degrees
  --decl_deg DECL_DEG   Declination - degrees
  --decl_min DECL_MIN   Declination - minutes
  --decl_sec DECL_SEC   Declination - seconds
  --degrees DEGREES     Degrees
  --decimal_hours DECIMAL_HOURS
                        Decimal hours. Input format: floating point number, e.g., 18.52416667
  --greenwich_date GREENWICH_DATE
                        Greenwich date. Input format: 'mm/dd/yyyy'. Fractional day is allowed, e.g., '6/19.75/2009'
  --geo_lat GEO_LAT     Geographical latitude. Input format: (+/-)##.##, e.g., -64.00
  --geo_long GEO_LONG   Geographical longitude. Input format: (+/-)##.##, e.g., -64.00
  --gst GST             Greenwich sidereal time. Input format: 'hh:mm:ss'
  --ha_hr HA_HR         Hour angle - hours.
  --ha_min HA_MIN       Hour angle - minutes.
  --ha_sec HA_SEC       Hour angle - seconds.
  --lst LST             Local sidereal time. Input format: 'hh:mm:ss'
  --jd JD               Julian date. Input format: floating point number, e.g., 2455002.25
  --minutes MINUTES     Minutes
  --seconds SECONDS     Seconds
  --ut UT               Universal time. Input format: 'hh:mm:ss'
  --year YEAR           Calendar year, e.g. 2019.

Inputs (time zone management):
  --daylight_savings_time
                        Observe daylight savings time.
  --standard_time       Observe standard time (default)
  --zone_correction ZONE_CORRECTION
                        Offset, in hours, for time zone correction.

```

### Example

Convert universal time to Greenwich sidereal time:

```
$./pa-cli.py --ut_to_gst --ut "14:36:51.67" --greenwich_date "4/22/1980"

{"greenwichSiderealTimeHours": 4, "greenwichSiderealTimeMinutes": 40, "greenwichSiderealTimeSeconds": 5.23}
```

## Unit Tests

Unit test run can be invoked via the Make utility:

```
make all
```
