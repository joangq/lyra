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

class Collection_insitu_comprehensive_upper_air_observation_network(Collection):
    collection_name = 'insitu-comprehensive-upper-air-observation-network'
    valid_values = dict(
        day = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31'],
        format = ['netcdf', 'csv'],
        month = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
        variable = ['air_pressure', 'air_temperature', 'dew_point_temperature', 'dew_point_depression', 'specific_humidity', 'relative_humidity', 'wind_speed', 'wind_from_direction', 'eastward_wind_speed', 'northward_wind_speed', 'geopotential_height', 'wind_bias_estimate', 'rise_bias_estimate', 'desroziers_30_uncertainty', 'humidity_bias_estimate'],
        year = ['1905', '1906', '1907', '1908', '1909', '1910', '1911', '1912', '1913', '1914', '1915', '1916', '1917', '1918', '1919', '1920', '1921', '1922', '1923', '1924', '1925', '1926', '1927', '1928', '1929', '1930', '1931', '1932', '1933', '1934', '1935', '1936', '1937', '1938', '1939', '1940', '1941', '1942', '1943', '1944', '1945', '1946', '1947', '1948', '1949', '1950', '1951', '1952', '1953', '1954', '1955', '1956', '1957', '1958', '1959', '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023'],
    )

    @Collection.wrapper
    def download(cls, day: OneOrMore[str], format: str, month: OneOrMore[str], variable: OneOrMore[str], year: OneOrMore[str], area_group: Union[FreeEditionType, GeographicExtentType] = 'global'): 
        """
        Parameters
        ----------
        :param day:
        :type day: str

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

        
        - 13

        
        - 14

        
        - 15

        
        - 16

        
        - 17

        
        - 18

        
        - 19

        
        - 20

        
        - 21

        
        - 22

        
        - 23

        
        - 24

        
        - 25

        
        - 26

        
        - 27

        
        - 28

        
        - 29

        
        - 30

        
        - 31

        ---

        :param format:
        :type format: str

        **Valid values:**
        
        - netcdf

        
        - csv

        ---

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

        :param variable:
        :type variable: str

        **Valid values:**
        
        - air_pressure

        
        - air_temperature

        
        - dew_point_temperature

        
        - dew_point_depression

        
        - specific_humidity

        
        - relative_humidity

        
        - wind_speed

        
        - wind_from_direction

        
        - eastward_wind_speed

        
        - northward_wind_speed

        
        - geopotential_height

        
        - wind_bias_estimate

        
        - rise_bias_estimate

        
        - desroziers_30_uncertainty

        
        - humidity_bias_estimate

        ---

        :param year:
        :type year: str

        **Valid values:**
        
        - 1905

        
        - 1906

        
        - 1907

        
        - 1908

        
        - 1909

        
        - 1910

        
        - 1911

        
        - 1912

        
        - 1913

        
        - 1914

        
        - 1915

        
        - 1916

        
        - 1917

        
        - 1918

        
        - 1919

        
        - 1920

        
        - 1921

        
        - 1922

        
        - 1923

        
        - 1924

        
        - 1925

        
        - 1926

        
        - 1927

        
        - 1928

        
        - 1929

        
        - 1930

        
        - 1931

        
        - 1932

        
        - 1933

        
        - 1934

        
        - 1935

        
        - 1936

        
        - 1937

        
        - 1938

        
        - 1939

        
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

        ---

        :param area_group:
        :type area_group: str

        ---

        Returns
        -------
        :return: The data requested
        :rtype: Any
        """
        UNREACHABLE()

def download_insitu_comprehensive_upper_air_observation_network(day: OneOrMore[str], format: str, month: OneOrMore[str], variable: OneOrMore[str], year: OneOrMore[str], area_group: Union[FreeEditionType, GeographicExtentType] = 'global'):
    return Collection_insitu_comprehensive_upper_air_observation_network.download(day=day, format=format, month=month, variable=variable, year=year, area_group=area_group)

