#DailyHigh -> TemperatureInfo -> AirTemperature
CLEAN_MAP = {
    "root": ['StationId'],
    "ObsTime": ['DateTime'],
    "WeatherElement": ['AirTemperature', 'RelativeHumidity', 'AirPressure', 'Weather', 'WindSpeed'],
    "DailyExtreme": ['DailyHigh', 'DailyLow'],
    "Now": ['Precipitation']
}

WeatherElement = ['AirTemperature', 'RelativeHumidity', 'AirPressure', 'WindSpeed']
def loadpulse_universal_cleaner(station_node):
    cleaned_result = {}
    if not station_node:
        return {}

    obs_time = station_node.get('ObsTime', {})
    elements = station_node.get('WeatherElement', {})
    daily_ext = elements.get('DailyExtreme', {})
    now_data = elements.get('Now', {})

    #layer 1
    cleaned_result['station_id'] = station_node.get('StationId')
    cleaned_result['obs_time'] = obs_time.get('DateTime') 

    #layer  WeatherElement
    for item in WeatherElement:
        raw_val = elements.get(item)
        cleaned_result[item.lower()]  = abnormal_value_composing(raw_val)
    
    #Other_layers:DailyHigh -> TemperatureInfo -> AirTemperature
    #Other_layer:Now -> Precipitation
    day_high = daily_ext.get('DailyHigh',{}).get('TemperatureInfo',{}).get('AirTemperature')
    cleaned_result['day_high'] = abnormal_value_composing(day_high)
    day_low = daily_ext.get('DailyLow',{}).get('TemperatureInfo',{}).get('AirTemperature')
    cleaned_result['day_low'] = abnormal_value_composing(day_low)
    rain  = now_data.get('Precipitation')
    cleaned_result['rain'] = abnormal_value_composing(rain)

    return cleaned_result

def abnormal_value_composing(data):
    try:
        val = float(data)
        return None if val == -99.0 else val
    except (TypeError, ValueError):
        return None
