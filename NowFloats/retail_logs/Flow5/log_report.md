**/on_search**
- /message/catalog/bpp~1providers/0/items/0/descriptor/images must NOT have more than 3 items
- /message/catalog/bpp~1providers/0/items/1/descriptor/images must NOT have more than 3 items

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

