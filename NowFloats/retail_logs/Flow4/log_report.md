**/on_search**
- /message/catalog/bpp~1providers/0/items/0/descriptor/images must NOT have more than 3 items
- /message/catalog/bpp~1providers/0/items/1/descriptor/images must NOT have more than 3 items

**/on_select**
- /fulfillments/0/state/descriptor/code must be equal to one of the allowed values (Serviceable,Non-serviceable)
- Pre-order fulfillment state codes should be used in fulfillments[].state.descriptor.code

**/init**
- /message/order/billing/address must have required property 'building'
- /message/order/fulfillments/0/end/location/address/building must NOT have fewer than 3 characters
- /message/order/fulfillments/0/end/location/address/locality must NOT have fewer than 3 characters
- billing/created_at should match context.timestamp
- billing/updated_at should match context.timestamp
- address.building should be more than 3 chars
- address.locality should be more than 3 chars

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

**/on_update (Initiated)**
-  must have required property 'payment'
-  must have required property 'created_at'
-  must have required property 'updated_at'
- /fulfillments/0/end must have required property 'time'
- /fulfillments/0/end/location/address must have required property 'building'
- Invalid quantity of items present in /order/items (returned & non-returned) for item: cae57369-9776-4e0d-9ec0-4c5b748de999
- order/created_at timestamp can't change (should remain same as in /confirm)

