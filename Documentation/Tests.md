Test the creation of a new UAV object:
a. Test that a UAV object can be created with valid data.
b. Test that a UAV object cannot be created with invalid data (e.g. missing required fields).

Test the retrieval of UAV objects:
a. Test that all UAV objects can be retrieved.
b. Test that a specific UAV object can be retrieved by ID.

Test the update of a UAV object:
a. Test that a UAV object can be updated with valid data.
b. Test that a UAV object cannot be updated with invalid data (e.g. missing required fields).

Test the deletion of a UAV object:
a. Test that a UAV object can be deleted.
b. Test that attempting to delete a non-existent UAV object raises an appropriate error.

Test the rental of a UAV:
a. Test that a UAV can be rented by setting the 'rented' field to True.
b. Test that a rented UAV cannot be updated or deleted.

Test the filtering of UAV objects:
a. Test that UAV objects can be filtered by brand, model, weight, category, and rented status.
b. Test that the correct number of UAV objects are returned when filtering with valid parameters.

Test the validation of UAV data:
a. Test that the weight field can only accept numeric values.
b. Test that the rented field can only accept boolean values.

Test the API endpoints:
a. Test that the UAV list API endpoint returns a list of all UAV objects.
b. Test that the UAV detail API endpoint returns the details of a specific UAV object.