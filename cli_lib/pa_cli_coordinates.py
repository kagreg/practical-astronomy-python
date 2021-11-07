import json
from dateutil.parser import parse
import lib.pa_coordinate as PA_CO
import cli_lib.pa_cli_util as PA_UTIL

class CliCoordinates:
	def __init__(self, args):
		self.args = args

	def eval_coordinates(self):
		'''
		Determine if any coordinates action args were passed.
		'''

		# Angle to Decimal Degrees
		if self.args.a_to_dd:
			if self.args.degrees == None:
				PA_UTIL.display_error("'degrees' argument is required.")
			elif self.args.minutes == None:
				PA_UTIL.display_error("'minutes' argument is required.")
			elif self.args.seconds == None:
				PA_UTIL.display_error("'seconds' argument is required.")
			else:
				self.a_to_dd(self.args.degrees, self.args.minutes, self.args.seconds)

		# Decimal Degrees to Angle
		if self.args.dd_to_a:
			if self.args.decimal_degrees == None:
				PA_UTIL.display_error("'decimal_degrees' argument is required.")
			else:
				self.dd_to_a(self.args.decimal_degrees)

		# Equatorial Coordinates to Horizontal Coordinates
		if self.args.ec_to_hc:
			if self.args.ha_hr == None:
				PA_UTIL.display_error("'ha_hr' argument is required.")
			elif self.args.ha_min == None:
				PA_UTIL.display_error("'ha_min' argument is required.")
			elif self.args.ha_sec == None:
				PA_UTIL.display_error("'ha_sec' argument is required.")
			elif self.args.decl_deg == None:
				PA_UTIL.display_error("'decl_deg' argument is required.")
			elif self.args.decl_min == None:
				PA_UTIL.display_error("'decl_min' argument is required.")
			elif self.args.decl_sec == None:
				PA_UTIL.display_error("'decl_sec' argument is required.")
			elif self.args.geo_lat == None:
				PA_UTIL.display_error("'geo_lat' argument is required.")
			else:
				self.ec_to_hc(self.args.ha_hr, self.args.ha_min, self.args.ha_sec, self.args.decl_deg, self.args.decl_min, self.args.decl_sec, self.args.geo_lat)

		# Horizontal Coordinates to Equatorial Coordinates
		if self.args.hc_to_ec:
			if self.args.az_deg == None:
				PA_UTIL.display_error("'az_deg' argument is required.")
			elif self.args.az_min == None:
				PA_UTIL.display_error("'az_min' argument is required.")
			elif self.args.az_sec == None:
				PA_UTIL.display_error("'az_sec' argument is required.")
			elif self.args.alt_deg == None:
				PA_UTIL.display_error("'alt_deg' argument is required.")
			elif self.args.alt_min == None:
				PA_UTIL.display_error("'alt_min' argument is required.")
			elif self.args.alt_sec == None:
				PA_UTIL.display_error("'alt_sec' argument is required.")
			elif self.args.geo_lat == None:
				PA_UTIL.display_error("'geo_lat' argument is required.")
			else:
				self.hc_to_ec(self.args.az_deg, self.args.az_min, self.args.az_sec, self.args.alt_deg, self.args.alt_min, self.args.alt_sec, self.args.geo_lat)

		# Mean obliquity of the ecliptic
		if self.args.mean_obliq_ecliptic:
			if self.args.greenwich_date == None:
				PA_UTIL.display_error("'greenwich_date' argument is required.")
			else:
				self.mean_obliq_ecliptic(self.args.greenwich_date)

		# Ecliptic coordinates to equatorial coordinates
		if self.args.ecl_c_to_equa_c:
			if self.args.ecl_long_deg == None:
				PA_UTIL.display_error("'ecl_long_deg' argument is required.")
			elif self.args.ecl_long_min == None:
				PA_UTIL.display_error("'ecl_long_min' argument is required.")
			elif self.args.ecl_long_sec == None:
				PA_UTIL.display_error("'ecl_long_sec' argument is required.")
			elif self.args.ecl_lat_deg == None:
				PA_UTIL.display_error("'ecl_lat_deg' argument is required.")
			elif self.args.ecl_lat_min == None:
				PA_UTIL.display_error("'ecl_lat_min' argument is required.")
			elif self.args.ecl_lat_sec == None:
				PA_UTIL.display_error("'ecl_lat_sec' argument is required.")
			elif self.args.greenwich_date == None:
				PA_UTIL.display_error("'greenwich_date' argument is required.")
			else:
				self.ecl_c_to_equa_c(self.args.ecl_long_deg, self.args.ecl_long_min, self.args.ecl_long_sec, self.args.ecl_lat_deg, self.args.ecl_lat_min, self.args.ecl_lat_sec, self.args.greenwich_date)

		# Equatorial coordinates to ecliptic coordinates
		if self.args.equa_c_to_ecl_c:
			if self.args.ra_hr == None:
				PA_UTIL.display_error("'ra_hr' argument is required.")
			elif self.args.ra_min == None:
				PA_UTIL.display_error("'ra_min' argument is required.")
			elif self.args.ra_sec == None:
				PA_UTIL.display_error("'ra_sec' argument is required.")
			elif self.args.decl_deg == None:
				PA_UTIL.display_error("'decl_deg' argument is required.")
			elif self.args.decl_min == None:
				PA_UTIL.display_error("'decl_min' argument is required.")
			elif self.args.decl_sec == None:
				PA_UTIL.display_error("'decl_sec' argument is required.")
			elif self.args.greenwich_date == None:
				PA_UTIL.display_error("'greenwich_date' argument is required.")
			else:
				self.equa_c_to_ecl_c(self.args.ra_hr, self.args.ra_min, self.args.ra_sec, self.args.decl_deg, self.args.decl_min, self.args.decl_sec, self.args.greenwich_date)

		# Equatorial coordinates to galactic coordinates
		if self.args.equa_c_to_gal_c:
			if self.args.ra_hr == None:
				PA_UTIL.display_error("'ra_hr' argument is required.")
			elif self.args.ra_min == None:
				PA_UTIL.display_error("'ra_min' argument is required.")
			elif self.args.ra_sec == None:
				PA_UTIL.display_error("'ra_sec' argument is required.")
			elif self.args.decl_deg == None:
				PA_UTIL.display_error("'decl_deg' argument is required.")
			elif self.args.decl_min == None:
				PA_UTIL.display_error("'decl_min' argument is required.")
			elif self.args.decl_sec == None:
				PA_UTIL.display_error("'decl_sec' argument is required.")
			else:
				self.equa_c_to_gal_c(self.args.ra_hr, self.args.ra_min, self.args.ra_sec, self.args.decl_deg, self.args.decl_min, self.args.decl_sec)

		# Galactic coordinates to equatorial coordinates
		if self.args.gal_c_to_equa_c:
			if self.args.gal_long_deg == None:
				PA_UTIL.display_error("'gal_long_deg' argument is required.")
			elif self.args.gal_long_min == None:
				PA_UTIL.display_error("'gal_long_min' argument is required.")
			elif self.args.gal_long_sec == None:
				PA_UTIL.display_error("'gal_long_sec' argument is required.")
			elif self.args.gal_lat_deg == None:
				PA_UTIL.display_error("'gal_lat_deg' argument is required.")
			elif self.args.gal_lat_min == None:
				PA_UTIL.display_error("'gal_lat_min' argument is required.")
			elif self.args.gal_lat_sec == None:
				PA_UTIL.display_error("'gal_lat_sec' argument is required.")
			else:
				self.gal_c_to_equa_c(self.args.gal_long_deg, self.args.gal_long_min, self.args.gal_long_sec, self.args.gal_lat_deg, self.args.gal_lat_min, self.args.gal_lat_sec)

		# Calculate angular distance between two objects
		if self.args.ang_b_two_obj:
			if self.args.ra_long1 == None:
				PA_UTIL.display_error("'ra_long1' argument is required.")
			elif self.args.decl_lat1 == None:
				PA_UTIL.display_error("'decl_lat1' argument is required.")
			elif self.args.ra_long2 == None:
				PA_UTIL.display_error("'ra_long2' argument is required.")
			elif self.args.decl_lat2 == None:
				PA_UTIL.display_error("'decl_lat2' argument is required.")
			elif self.args.h_or_d == None:
				PA_UTIL.display_error("'h_or_d' argument is required.")
			else:
				self.ang_b_two_obj(self.args.ra_long1, self.args.decl_lat1, self.args.ra_long2, self.args.decl_lat2, self.args.h_or_d)

		# Calculate rise and set times
		if self.args.rise_and_set:
			if self.args.ra_hr == None:
				PA_UTIL.display_error("'ra_hr' argument is required.")
			elif self.args.ra_min == None:
				PA_UTIL.display_error("'ra_min' argument is required.")
			elif self.args.ra_sec == None:
				PA_UTIL.display_error("'ra_sec' argument is required.")
			elif self.args.decl_deg == None:
				PA_UTIL.display_error("'decl_deg' argument is required.")
			elif self.args.decl_min == None:
				PA_UTIL.display_error("'decl_min' argument is required.")
			elif self.args.decl_sec == None:
				PA_UTIL.display_error("'decl_sec' argument is required.")
			elif self.args.greenwich_date == None:
				PA_UTIL.display_error("'greenwich_date' argument is required.")
			elif self.args.geo_long == None:
				PA_UTIL.display_error("'geo_long' argument is required.")
			elif self.args.geo_lat == None:
				PA_UTIL.display_error("'geo_lat' argument is required.")
			elif self.args.v_sh_deg == None:
				PA_UTIL.display_error("'v_sh_deg' argument is required.")
			else:
				self.rise_and_set(self.args.ra_hr, self.args.ra_min, self.args.ra_sec, self.args.decl_deg, self.args.decl_min, self.args.decl_sec, self.args.greenwich_date, self.args.geo_long, self.args.geo_lat, self.args.v_sh_deg)

		# Calculate precession
		if self.args.precession:
			if self.args.ra_hr == None:
				PA_UTIL.display_error("'ra_hr' argument is required.")
			elif self.args.ra_min == None:
				PA_UTIL.display_error("'ra_min' argument is required.")
			elif self.args.ra_sec == None:
				PA_UTIL.display_error("'ra_sec' argument is required.")
			elif self.args.decl_deg == None:
				PA_UTIL.display_error("'decl_deg' argument is required.")
			elif self.args.decl_min == None:
				PA_UTIL.display_error("'decl_min' argument is required.")
			elif self.args.decl_sec == None:
				PA_UTIL.display_error("'decl_sec' argument is required.")
			elif self.args.epoch1 == None:
				PA_UTIL.display_error("'epoch1' argument is required.")
			elif self.args.epoch2 == None:
				PA_UTIL.display_error("'epoch2' argument is required.")
			else:
				self.precession(self.args.ra_hr, self.args.ra_min, self.args.ra_sec, self.args.decl_deg, self.args.decl_min, self.args.decl_sec, self.args.epoch1, self.args.epoch2)

		# Calculate nutation
		if self.args.nutation:
			if self.args.greenwich_date == None:
				PA_UTIL.display_error("'greenwich_date' argument is required.")
			else:
				self.nutation(self.args.greenwich_date)

	def nutation(self, greenwich_date):
		dt = parse(greenwich_date)

		nut_in_long_deg, nut_in_obl_deg = PA_CO.nutation_in_ecliptic_longitude_and_obliquity(dt.day, dt.month, dt.year)

		nut_in_long_deg = round(nut_in_long_deg,9)
		nut_in_obl_deg = round(nut_in_obl_deg,7)

		nutation_dict = dict(nutationInEclipticLongitude=nut_in_long_deg, nutationInEclipticObliquity=nut_in_obl_deg)

		print(json.dumps(nutation_dict))

	def precession(self, ra_hours, ra_minutes, ra_seconds, decl_degrees, decl_minutes, decl_seconds, epoch1, epoch2):
		'''
		Calculate precession.
		'''
		epoch1_split = epoch1.split("/")
		epoch2_split = epoch2.split("/")

		corrected_ra_hour, corrected_ra_minutes, corrected_ra_seconds, corrected_dec_deg, corrected_dec_minutes, corrected_dec_seconds = PA_CO.correct_for_precession(ra_hours, ra_minutes, ra_seconds, decl_degrees, decl_minutes, decl_seconds, float(epoch1_split[1]), float(epoch1_split[0]), float(epoch1_split[2]), float(epoch2_split[1]), float(epoch2_split[0]), float(epoch2_split[2]))

		precession_dict = dict(correctedRightAscensionHour=corrected_ra_hour, correctedRightAscensionMinutes=corrected_ra_minutes, correctedRightAscensionSeconds=corrected_ra_seconds, correctedDeclinationDegrees=corrected_dec_deg, correctedDeclinationMinutes=corrected_dec_minutes, correctedDeclinationSeconds=corrected_dec_seconds)

		print(json.dumps(precession_dict))

	def a_to_dd(self, degrees, minutes, seconds):
		'''
		Convert angle (degrees, minutes, and seconds) to decimal degrees.
		'''
		decimal_degrees = PA_CO.angle_to_decimal_degrees(degrees, minutes, seconds)
		decimal_degrees = round(decimal_degrees, 7)
		decimal_degrees_dict = dict(decimalDegrees=decimal_degrees)

		print(json.dumps(decimal_degrees_dict))

	def dd_to_a(self, decimal_degrees):
		'''
		Convert decimal degrees to angle (degrees, minutes, and seconds).
		'''
		degrees,minutes,seconds = PA_CO.decimal_degrees_to_angle(decimal_degrees)
		degrees_dict = dict(degrees=degrees, minutes=minutes,seconds=seconds)

		print(json.dumps(degrees_dict))

	def ec_to_hc(self, hour_angle_hours, hour_angle_minutes, hour_angle_seconds, declination_degrees, declination_minutes, declination_seconds, geographical_latitude):
		'''
		Convert equatorial coordinates to horizontal coordinates
		'''
		azimuth_degrees, azimuth_minutes, azimuth_seconds, altitude_degrees, altitude_minutes, altitude_seconds = PA_CO.equatorial_coordinates_to_horizon_coordinates(hour_angle_hours, hour_angle_minutes, hour_angle_seconds, declination_degrees, declination_minutes, declination_seconds, geographical_latitude)
		
		eq_coord_dict = dict(azimuthDegrees=azimuth_degrees, azimuthMinutes=azimuth_minutes, azimuthSeconds=azimuth_seconds, altitudeDegrees=altitude_degrees, altitudeMinutes=altitude_minutes, altitudeSeconds=altitude_seconds)

		print(json.dumps(eq_coord_dict))

	def hc_to_ec(self, azimuth_degrees, azimuth_minutes, azimuth_seconds, altitude_degrees, altitude_minutes, altitude_seconds, geographical_latitude):
		'''
		Convert horizontal coordinates to equatorial coordinates
		'''
		hour_angle_hours, hour_angle_minutes, hour_angle_seconds, declination_degrees, declination_minutes, declination_seconds = PA_CO.horizon_coordinates_to_equatorial_coordinates(azimuth_degrees, azimuth_minutes, azimuth_seconds, altitude_degrees, altitude_minutes, altitude_seconds, geographical_latitude)

		hc_coord_dict = dict(hourAngleHours=hour_angle_hours, hourAngleMinutes=hour_angle_minutes, hourAngleSeconds=hour_angle_seconds, declinationDegrees=declination_degrees, declinationMinutes=declination_minutes, declinationSeconds=declination_seconds, geographicalLatitude=geographical_latitude)

		print(json.dumps(hc_coord_dict))

	def mean_obliq_ecliptic(self, greenwich_date):
		'''
		Calculate mean obliquity of the ecliptic
		'''
		dt = parse(greenwich_date)
		obliquity = PA_CO.mean_obliquity_of_the_ecliptic(dt.day, dt.month, dt.year)
		obliquity = round(obliquity,8)
		obliquity_dict = dict(obliquity=obliquity)

		print(json.dumps(obliquity_dict))

	def ecl_c_to_equa_c(self, ecl_long_deg, ecl_long_min, ecl_long_sec, ecl_lat_deg, ecl_lat_min, ecl_lat_sec, greenwich_date):
		'''
		Convert ecliptic coordinates to equatorial coordinates
		'''
		dt = parse(greenwich_date)
		ra_hours,ra_minutes,ra_seconds,dec_degrees,dec_minutes,dec_seconds = PA_CO.ecliptic_coordinate_to_equatorial_coordinate(ecl_long_deg, ecl_long_min, ecl_long_sec, ecl_lat_deg, ecl_lat_min, ecl_lat_sec, dt.day, dt.month, dt.year)
		equa_c_dict = dict(rightAscensionHours=ra_hours, rightAscensionMinutes=ra_minutes, rightAscensionSeconds=ra_seconds, declinationDegrees=dec_degrees, declinationMinutes=dec_minutes, declinationSeconds=dec_seconds)

		print(json.dumps(equa_c_dict))

	def equa_c_to_ecl_c(self, ra_hours, ra_minutes, ra_seconds, decl_degrees, decl_minutes, decl_seconds, greenwich_date):
		'''
		Convert equatorial coordinates to ecliptic coordinates
		'''
		dt = parse(greenwich_date)
		ecl_long_deg,ecl_long_min,ecl_long_sec,ecl_lat_deg,ecl_lat_min,ecl_lat_sec = PA_CO.equatorial_coordinate_to_ecliptic_coordinate(ra_hours,ra_minutes,ra_seconds,decl_degrees,decl_minutes,decl_seconds,dt.day,dt.month,dt.year)
		ecl_c_dict = dict(eclipticLongitudeDegrees=ecl_long_deg,eclipticLongitudeMinutes=ecl_long_min,eclipticLongitudeSeconds=ecl_long_sec,eclipticLatitudeDegrees=ecl_lat_deg,eclipticLatitudeMinutes=ecl_lat_min,eclipticLatitudeSeconds=ecl_lat_sec)

		print(json.dumps(ecl_c_dict))

	def equa_c_to_gal_c(self, ra_hours, ra_minutes, ra_seconds, decl_degrees, decl_minutes, decl_seconds):
		'''
		Convert equatorial coordinates to galactic coordinates
		'''
		gal_long_deg, gal_long_min, gal_long_sec, gal_lat_deg, gal_lat_min, gal_lat_sec = PA_CO.equatorial_coordinate_to_galactic_coordinate(ra_hours, ra_minutes, ra_seconds, decl_degrees, decl_minutes, decl_seconds)
		gal_c_dict = dict(galacticLongitudeDegrees=gal_long_deg,galacticLongitudeMinutes=gal_long_min,galacticLongitudeSeconds=gal_long_sec,galacticLatitudeDegrees=gal_lat_deg,galacticLatitudeMinutes=gal_lat_min,galacticLatitudeSeconds=gal_lat_sec)

		print(json.dumps(gal_c_dict))

	def gal_c_to_equa_c(self, gal_long_deg, gal_long_min, gal_long_sec, gal_lat_deg, gal_lat_min, gal_lat_sec):
		'''
		Convert galactic coordinates to equatorial coordinates
		'''
		ra_hours, ra_minutes, ra_seconds, dec_degrees, dec_minutes, dec_seconds = PA_CO.galactic_coordinate_to_equatorial_coordinate(gal_long_deg, gal_long_min, gal_long_sec, gal_lat_deg, gal_lat_min, gal_lat_sec)
		equa_c_dict = dict(rightAscensionHours=ra_hours, rightAscensionMinutes=ra_minutes, rightAscensionSeconds=ra_seconds, declinationDegrees=dec_degrees, declinationMinutes=dec_minutes, declinationSeconds=dec_seconds)

		print(json.dumps(equa_c_dict))

	def ang_b_two_obj(self, ra_long1, decl_lat1, ra_long2, decl_lat2, h_or_d):
		'''
		Calculate angle between two objects.
		'''
		ra_long1_split = ra_long1.split(":")
		decl_lat1_split = decl_lat1.split(":")
		ra_long2_split = ra_long2.split(":")
		decl_lat2_split = decl_lat2.split(":")

		angle_deg, angle_min, angle_sec = PA_CO.angle_between_two_objects(float(ra_long1_split[0]), float(ra_long1_split[1]), float(ra_long1_split[2]), float(decl_lat1_split[0]), float(decl_lat1_split[1]), float(decl_lat1_split[2]), float(ra_long2_split[0]), float(ra_long2_split[1]), float(ra_long2_split[2]), float(decl_lat2_split[0]), float(decl_lat2_split[1]), float(decl_lat2_split[2]), h_or_d)

		angle_dict = dict(angleDegrees=angle_deg, angleMinutes=angle_min, angleSeconds=angle_sec)

		print(json.dumps(angle_dict))

	def rise_and_set(self, ra_hours, ra_minutes, ra_seconds, decl_degrees, decl_minutes, decl_seconds, greenwich_date, geo_long, geo_lat, v_sh_deg):
		'''
		Calculate rise and set times.
		'''
		dt = parse(greenwich_date)

		rise_set_status, ut_rise_hour, ut_rise_min, ut_set_hour, ut_set_min, az_rise, az_set = PA_CO.rising_and_setting(ra_hours, ra_minutes, ra_seconds, decl_degrees, decl_minutes, decl_seconds, dt.day, dt.month, dt.year, geo_long, geo_lat, v_sh_deg)

		rise_set_dict = dict(riseSetStatus=rise_set_status, universalTimeRiseHour=ut_rise_hour, universalTimeRiseMinutes=ut_rise_min, universalTimeSetHour=ut_set_hour, universalTimeSetMinutes=ut_set_min, azimuthRise=az_rise, azimuthSet=az_set)

		print(json.dumps(rise_set_dict))
