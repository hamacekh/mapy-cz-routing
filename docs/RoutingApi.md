# mapy_cz_routing.RoutingApi

All URIs are relative to *https://api.mapy.cz*

Method | HTTP request | Description
------------- | ------------- | -------------
[**basic_route_v1_routing_route_get**](RoutingApi.md#basic_route_v1_routing_route_get) | **GET** /v1/routing/route | Basic Route


# **basic_route_v1_routing_route_get**
> ResponseBasicRouteV1RoutingRouteGet basic_route_v1_routing_route_get(start, end, route_type, lang=lang, format=format, avoid_toll=avoid_toll, waypoints=waypoints)

Basic Route

Service for finding/planning a route between two points, optionally via up to fifteen waypoints. The result of the planner call is the length of the found route, the estimated duration according to the selected mode of transport and the geometry of the route in the selected format. If it is not possible to plan the route for the selected mode of transport, the service will return http response code ``404``. The cause of the error is described in the response body: ```json { \"detail\": [     {         \"msg\": \"Edge not found\",         \"errorCode\": 7,     }     ] } ``` ### Possible routing errors: * ``errorCode: 7`` - the route point is outside the available route network for the selected type of transport. * ``errorCode: 9`` - the route point is located in an area to which is not connected by the selected mode of transport. For example, another continent.

### Example

* Api Key Authentication (headerApiKey):
* Api Key Authentication (queryApiKey):

```python
import time
import os
import mapy_cz_routing
from mapy_cz_routing.models.response_basic_route_v1_routing_route_get import ResponseBasicRouteV1RoutingRouteGet
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
with mapy_cz_routing.ApiClient(configuration) as api_client:
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
        api_response = api_instance.basic_route_v1_routing_route_get(start, end, route_type, lang=lang, format=format, avoid_toll=avoid_toll, waypoints=waypoints)
        print("The response of RoutingApi->basic_route_v1_routing_route_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RoutingApi->basic_route_v1_routing_route_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start** | [**object**](.md)| Coordinates of the beginning of the route. An array of two float numbers. The first number is &#x60;&#x60;longitude&#x60;&#x60;, the second is &#x60;&#x60;latitude&#x60;&#x60;. Supports exploded &#x60;&#x60;?start&#x3D;14.40094&amp;start&#x3D;50.0711&#x60;&#x60; and unexploded &#x60;&#x60;?start&#x3D;14.40094,50.0711&#x60;&#x60; format. | 
 **end** | [**object**](.md)| Coordinates of the end of the route. An array of two float numbers. The first number is &#x60;&#x60;longitude&#x60;&#x60;, the second is &#x60;&#x60;latitude&#x60;&#x60;. Supports exploded &#x60;&#x60;?end&#x3D;14.40094&amp;end&#x3D;50.0711&#x60;&#x60; and unexploded &#x60;&#x60;?end&#x3D;14.40094,50.0711&#x60;&#x60; format. | 
 **route_type** | [**RouteType**](.md)| Route type | 
 **lang** | [**Language**](.md)| Language | [optional] 
 **format** | [**GeometryFormat**](.md)| Output geometry format | [optional] 
 **avoid_toll** | [**object**](.md)| Avoid sections where tolls are paid | [optional] 
 **waypoints** | [**object**](.md)| Up to 15 optional waypoint coordinates between start and end.  The parameter supports a semicolon-separated list of coordinates &#x60;&#x60;?waypoints&#x3D;14.4009400,50.0711000;14.3951303,50.0704094&#x60;&#x60;, or exploded array of coordinates &#x60;&#x60;?waypoints&#x3D;14.4009400,50.0711000&amp;waypoints&#x3D;14.3951303,50.0704094&#x60;&#x60;. The waypoint coordinates are two float numbers separated by a comma in the order &#x60;&#x60;longitude&#x60;&#x60;, &#x60;&#x60;latitude&#x60;&#x60;. | [optional] 

### Return type

[**ResponseBasicRouteV1RoutingRouteGet**](ResponseBasicRouteV1RoutingRouteGet.md)

### Authorization

[headerApiKey](../README.md#headerApiKey), [queryApiKey](../README.md#queryApiKey)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | In case it is not possible to plan a route according to the selected parameters. |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

