# mapy-cz-routing
Service for finding/planning a route between two or more points. 

Api is based on common principles described in the document [Common principles of REST API Mapy.cz](/v1/docs/commons/)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/hamacekh/mapy-cz-routing.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/hamacekh/mapy-cz-routing.git`)

Then import the package:
```python
import mapy_cz_routing
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import mapy_cz_routing
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import mapy_cz_routing
from mapy_cz_routing.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.mapy.cz
# See configuration.py for a list of all supported configuration parameters.
configuration = mapy_cz_routing.Configuration(
    host = "https://api.mapy.cz"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: headerApiKey
configuration.api_key['headerApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['headerApiKey'] = 'Bearer'

# Configure API key authorization: queryApiKey
configuration.api_key['queryApiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['queryApiKey'] = 'Bearer'


# Enter a context with an instance of the API client
async with mapy_cz_routing.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = mapy_cz_routing.RoutingApi(api_client)
    start = [14.40094,50.0711] # object | Coordinates of the beginning of the route. An array of two float numbers. The first number is ``longitude``, the second is ``latitude``. Supports exploded ``?start=14.40094&start=50.0711`` and unexploded ``?start=14.40094,50.0711`` format.
    end = [16.5990122,49.1718222] # object | Coordinates of the end of the route. An array of two float numbers. The first number is ``longitude``, the second is ``latitude``. Supports exploded ``?end=14.40094&end=50.0711`` and unexploded ``?end=14.40094,50.0711`` format.
    route_type = mapy_cz_routing.RouteType() # RouteType | Route type
    lang = mapy_cz_routing.Language() # Language | Language (optional)
    format = mapy_cz_routing.GeometryFormat() # GeometryFormat | Output geometry format (optional)
    avoid_toll = None # object | Avoid sections where tolls are paid (optional)
    waypoints = ["15.5903861, 49.3967233","16.4187328, 49.3414642"] # object | Up to 15 optional waypoint coordinates between start and end.  The parameter supports a semicolon-separated list of coordinates ``?waypoints=14.4009400,50.0711000;14.3951303,50.0704094``, or exploded array of coordinates ``?waypoints=14.4009400,50.0711000&waypoints=14.3951303,50.0704094``. The waypoint coordinates are two float numbers separated by a comma in the order ``longitude``, ``latitude``. (optional)

    try:
        # Basic Route
        api_response = await api_instance.basic_route_v1_routing_route_get(start, end, route_type, lang=lang, format=format, avoid_toll=avoid_toll, waypoints=waypoints)
        print("The response of RoutingApi->basic_route_v1_routing_route_get:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling RoutingApi->basic_route_v1_routing_route_get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.mapy.cz*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*RoutingApi* | [**basic_route_v1_routing_route_get**](docs/RoutingApi.md#basic_route_v1_routing_route_get) | **GET** /v1/routing/route | Basic Route


## Documentation For Models

 - [ErrorResponse](docs/ErrorResponse.md)
 - [FeatureType](docs/FeatureType.md)
 - [GeoJSONGeometry](docs/GeoJSONGeometry.md)
 - [GeoJSONLineString](docs/GeoJSONLineString.md)
 - [Geometry](docs/Geometry.md)
 - [GeometryFormat](docs/GeometryFormat.md)
 - [GeometryType](docs/GeometryType.md)
 - [HTTPValidationError](docs/HTTPValidationError.md)
 - [Language](docs/Language.md)
 - [Point](docs/Point.md)
 - [ResponseBasicRouteV1RoutingRouteGet](docs/ResponseBasicRouteV1RoutingRouteGet.md)
 - [RouteType](docs/RouteType.md)
 - [RoutingError](docs/RoutingError.md)
 - [RoutingErrorResponse](docs/RoutingErrorResponse.md)
 - [RoutingResponse](docs/RoutingResponse.md)
 - [ValidationError](docs/ValidationError.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="headerApiKey"></a>
### headerApiKey

- **Type**: API key
- **API key parameter name**: X-Mapy-Api-Key
- **Location**: HTTP header

<a id="queryApiKey"></a>
### queryApiKey

- **Type**: API key
- **API key parameter name**: apikey
- **Location**: URL query string


## Author




