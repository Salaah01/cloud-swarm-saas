/**Updates an oldObject using properties defined in a new object whilst
 * maintaining immutability by returning a copy of oldObject with the updated
 * properties.
 *
 * Args:
 *    oldObject: (obj) An object to be updated
 *    updatedProperties: (obj) An object consisting of properties to be
 *      added/updated onto the oldObject.
 */
export const updateObject = (
  oldObject: object,
  updatedProperties: object
): object => {
  return {
    ...oldObject,
    ...updatedProperties,
  };
};
