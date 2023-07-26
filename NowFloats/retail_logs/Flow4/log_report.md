**/on_search**
- /message/catalog/bpp~1providers/0/items/0/descriptor/images must NOT have more than 3 items
- /message/catalog/bpp~1providers/0/items/1/descriptor/images must NOT have more than 3 items

**/on_select**
- /fulfillments/0/state/descriptor/code must be equal to one of the allowed values (Serviceable,Non-serviceable)
- Pre-order fulfillment state codes should be used in fulfillments[].state.descriptor.code

**/init**
- /message/order/billing/address must have required property 'building'


**/on_init**
- /billing/address must have required property 'building'
- Discrepancies between the quote object in /on_select and /on_init

**/confirm**
- /message/order/billing/address must have required property 'building'
- order.created_at timestamp should match context.timestamp
- Discrepancies between the quote object in /on_select and /confirm

**/on_confirm**
- /billing/address must have required property 'building'
- /fulfillments/0/end/location/address must have required property 'building'
- Discrepancies between the quote object /on_select and /on_confirm

**/update**
- /message/order/items/0/tags/ttl_approval must match format "duration"



