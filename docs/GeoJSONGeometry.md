# GeoJSONGeometry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**FeatureType**](FeatureType.md) |  | 
**geometry** | [**GeoJSONLineString**](GeoJSONLineString.md) |  | 
**properties** | **object** |  | [optional] 

## Example

```python
from mapy_cz_routing.models.geo_json_geometry import GeoJSONGeometry

# TODO update the JSON string below
json = "{}"
# create an instance of GeoJSONGeometry from a JSON string
geo_json_geometry_instance = GeoJSONGeometry.from_json(json)
# print the JSON string representation of the object
print GeoJSONGeometry.to_json()

# convert the object into a dict
geo_json_geometry_dict = geo_json_geometry_instance.to_dict()
# create an instance of GeoJSONGeometry from a dict
geo_json_geometry_form_dict = geo_json_geometry.from_dict(geo_json_geometry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


