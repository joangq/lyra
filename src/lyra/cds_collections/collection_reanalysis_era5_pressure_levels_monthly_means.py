from lyra.translator import Collection
from lyra.common import OneOrMore
from lyra.common import GeographicExtentType
from lyra.common import GeographicExtentMapType
from lyra.common import LabelType
from lyra.common import FreeEditionType
from lyra.common import UNREACHABLE
from typing import Union, Optional

"""
This code has been automatically generated
by Lyra. Specifically, the format for
this code can be found in

`lyra.translator.translate`
"""

class Collection_reanalysis_era5_pressure_levels_monthly_means(Collection):
    collection_name = 'reanalysis-era5-pressure-levels-monthly-means'
    valid_values = dict(
        month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
        pressure_level = ['1', '2', '3', '5', '7', '10', '20', '30', '50', '70', '100', '125', '150', '175', '200', '225', '250', '300', '350', '400', '450', '500', '550', '600', '650', '700', '750', '775', '800', '825', '850', '875', '900', '925', '950', '975', '1000'],
        product_type = ['monthly_averaged_reanalysis', 'monthly_averaged_reanalysis_by_hour_of_day', 'monthly_averaged_ensemble_members', 'monthly_averaged_ensemble_members_by_hour_of_day'],
        time = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', '06:00', '07:00', '08:00', '09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00'],
        variable = ['divergence', 'fraction_of_cloud_cover', 'geopotential', 'ozone_mass_mixing_ratio', 'potential_vorticity', 'relative_humidity', 'specific_cloud_ice_water_content', 'specific_cloud_liquid_water_content', 'specific_humidity', 'specific_rain_water_content', 'specific_snow_water_content', 'temperature', 'u_component_of_wind', 'v_component_of_wind', 'vertical_velocity', 'vorticity'],
        year = ['1940', '1941', '1942', '1943', '1944', '1945', '1946', '1947', '1948', '1949', '1950', '1951', '1952', '1953', '1954', '1955', '1956', '1957', '1958', '1959', '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024'],
        data_format = ['grib', 'netcdf'],
        download_format = ['unarchived', 'zip'],
    )

    @Collection.wrapper
    def download(cls, month: OneOrMore[str], pressure_level: OneOrMore[str], product_type: OneOrMore[str], time: OneOrMore[str], variable: OneOrMore[str], year: OneOrMore[str], area_group: Union[FreeEditionType, GeographicExtentType] = 'global', data_format: str = 'grib', download_format: str = 'unarchived'): 
        """
        Parameters
        ----------
        :param month:
        :type month: str

        **Valid values:**
        
        - 01

        
        - 02

        
        - 03

        
        - 04

        
        - 05

        
        - 06

        
        - 07

        
        - 08

        
        - 09

        
        - 10

        
        - 11

        
        - 12

        ---

        :param pressure_level:
        :type pressure_level: str

        **Valid values:**
        
        - 1

        
        - 2

        
        - 3

        
        - 5

        
        - 7

        
        - 10

        
        - 20

        
        - 30

        
        - 50

        
        - 70

        
        - 100

        
        - 125

        
        - 150

        
        - 175

        
        - 200

        
        - 225

        
        - 250

        
        - 300

        
        - 350

        
        - 400

        
        - 450

        
        - 500

        
        - 550

        
        - 600

        
        - 650

        
        - 700

        
        - 750

        
        - 775

        
        - 800

        
        - 825

        
        - 850

        
        - 875

        
        - 900

        
        - 925

        
        - 950

        
        - 975

        
        - 1000

        ---

        :param product_type:
        :type product_type: str

        **Valid values:**
        
        - monthly_averaged_reanalysis

        
        - monthly_averaged_reanalysis_by_hour_of_day

        
        - monthly_averaged_ensemble_members

        
        - monthly_averaged_ensemble_members_by_hour_of_day

        ---

        :param time:
        :type time: str

        **Valid values:**
        
        - 00:00

        
        - 01:00

        
        - 02:00

        
        - 03:00

        
        - 04:00

        
        - 05:00

        
        - 06:00

        
        - 07:00

        
        - 08:00

        
        - 09:00

        
        - 10:00

        
        - 11:00

        
        - 12:00

        
        - 13:00

        
        - 14:00

        
        - 15:00

        
        - 16:00

        
        - 17:00

        
        - 18:00

        
        - 19:00

        
        - 20:00

        
        - 21:00

        
        - 22:00

        
        - 23:00

        ---

        :param variable:
        :type variable: str

        **Valid values:**
        
        - divergence

        
        - fraction_of_cloud_cover

        
        - geopotential

        
        - ozone_mass_mixing_ratio

        
        - potential_vorticity

        
        - relative_humidity

        
        - specific_cloud_ice_water_content

        
        - specific_cloud_liquid_water_content

        
        - specific_humidity

        
        - specific_rain_water_content

        
        - specific_snow_water_content

        
        - temperature

        
        - u_component_of_wind

        
        - v_component_of_wind

        
        - vertical_velocity

        
        - vorticity

        ---

        :param year:
        :type year: str

        **Valid values:**
        
        - 1940

        
        - 1941

        
        - 1942

        
        - 1943

        
        - 1944

        
        - 1945

        
        - 1946

        
        - 1947

        
        - 1948

        
        - 1949

        
        - 1950

        
        - 1951

        
        - 1952

        
        - 1953

        
        - 1954

        
        - 1955

        
        - 1956

        
        - 1957

        
        - 1958

        
        - 1959

        
        - 1960

        
        - 1961

        
        - 1962

        
        - 1963

        
        - 1964

        
        - 1965

        
        - 1966

        
        - 1967

        
        - 1968

        
        - 1969

        
        - 1970

        
        - 1971

        
        - 1972

        
        - 1973

        
        - 1974

        
        - 1975

        
        - 1976

        
        - 1977

        
        - 1978

        
        - 1979

        
        - 1980

        
        - 1981

        
        - 1982

        
        - 1983

        
        - 1984

        
        - 1985

        
        - 1986

        
        - 1987

        
        - 1988

        
        - 1989

        
        - 1990

        
        - 1991

        
        - 1992

        
        - 1993

        
        - 1994

        
        - 1995

        
        - 1996

        
        - 1997

        
        - 1998

        
        - 1999

        
        - 2000

        
        - 2001

        
        - 2002

        
        - 2003

        
        - 2004

        
        - 2005

        
        - 2006

        
        - 2007

        
        - 2008

        
        - 2009

        
        - 2010

        
        - 2011

        
        - 2012

        
        - 2013

        
        - 2014

        
        - 2015

        
        - 2016

        
        - 2017

        
        - 2018

        
        - 2019

        
        - 2020

        
        - 2021

        
        - 2022

        
        - 2023

        
        - 2024

        ---

        :param area_group:
        :type area_group: str

        ---

        :param data_format:
        :type data_format: str

        **Valid values:**
        
        - grib

        
        - netcdf

        ---

        :param download_format:
        :type download_format: str

        **Valid values:**
        
        - unarchived

        
        - zip

        ---

        Returns
        -------
        :return: The data requested
        :rtype: Any
        """
        UNREACHABLE()

def download_reanalysis_era5_pressure_levels_monthly_means(month: OneOrMore[str], pressure_level: OneOrMore[str], product_type: OneOrMore[str], time: OneOrMore[str], variable: OneOrMore[str], year: OneOrMore[str], area_group: Union[FreeEditionType, GeographicExtentType] = 'global', data_format: str = 'grib', download_format: str = 'unarchived'):
    return Collection_reanalysis_era5_pressure_levels_monthly_means.download(month=month, pressure_level=pressure_level, product_type=product_type, time=time, variable=variable, year=year, area_group=area_group, data_format=data_format, download_format=download_format)

