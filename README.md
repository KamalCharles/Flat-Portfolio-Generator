# OED Flat Portfolio generator

This script extracts the latitude and longitude of a selected country from either (Africa_EU_Asia_10km_inland.csv or America_10km_inland.csv) and creates a  location.csv file with the required OED (Open Exposure Data) columns for running a model. The required columns include data about the location such as construction code, occupancy code, peril covered, location currency, and others.

*Requirements*

    Python 3.x
    csv and json libraries
    
    
   ## Inputs

The script takes the following inputs:

    1. A CSV file with location data. The file should have columns for latitude, longitude, and country code.
    
    2.  A JSON configuration file with the following fields:
    
        country_code: the country code to filter the location data by.
        peril: the peril to be added to the transformed location data.
        LocCurrency: the location currency to be added to the transformed location data.
        data_file: the file name for the location data that you would like to extract from

### Configuration example
    
config.json file with the following information:


```javascript
{
  "country_code": "US",
  "peril": "EQ",
  "LocCurrency": "USD",
  "data_file": "Africa_EU_Asia_10km_inland.csv"
}
```
    

### How to Use

    Update the config.json file with the relevant information (country code, peril, location currency and the data file to extract from).
    Run the script using the command python 
    
    
>python Flatportfolio.py
    
    


### Output

The script generates a new CSV file with the following columns:

    *PortNumber
    *Latitude
    *Longitude
    *CountryCode
    *ConstructionCode
    *OccupancyCode
    *LocPerilsCovered
    *AccNumber
    *LocNumber
    *LocCurrency
    *OtherTIV
    *GeogName1
    *GeogScheme1

## License

This project is licensed under the MIT License.
