**/on_search**
- /message/catalog/bpp~1providers/0/items/0/descriptor/images must NOT have more than 3 items
- /message/catalog/bpp~1providers/0/items/1/descriptor/images must NOT have more than 3 items

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

