**/on_search**
- /message/catalog/bpp~1providers/0/items/0/descriptor/images must NOT have more than 3 items

**/select**
- /context/action must be equal to constant (select)
- context.action should be select
- Item Id e9511f3c-4592-4d7b-b038-ae5b6b1a58e5 does not exist in /on_search

**/on_select**
- Timestamp for /select api cannot be greater than or equal to /on_select api
- item with id: e9511f3c-4592-4d7b-b038-ae5b6b1a58e5 is not present in /on_search

**/init**
- /context/action must be equal to constant (init)
- /message/order/billing/address must have required property 'building'
- /message/order/fulfillments/0/end/location/address/building must NOT have fewer than 3 characters
- /message/order/fulfillments/0/end/location/address/locality must NOT have fewer than 3 characters
- context.action should be init
- billing/created_at should match context.timestamp
- billing/updated_at should match context.timestamp
- address.building should be more than 3 chars
- address.locality should be more than 3 chars

**/on_init**
- /billing/address must have required property 'building'
- Timestamp for init api cannot be greater than or equal to on_init api
- Discrepancies between the quote object in /on_select and /on_init

**/confirm**
- /context/action must be equal to constant (confirm)
- /message/order/billing/address must have required property 'building'
- context.action should be confirm
- order.created_at timestamp should match context.timestamp
- Discrepancies between the quote object in /on_select and /confirm

**/on_confirm**
- /billing/address must have required property 'building'
- /fulfillments/0/end/location/address must have required property 'building'
- Timestamp for /confirm api cannot be greater than or equal to /on_confirm api
- items[0].fulfillment_id mismatches for Item e9511f3c-4592-4d7b-b038-ae5b6b1a58e5 in /on_select and /on_confirm
- items[1].fulfillment_id mismatches for Item 66d697f7-2937-475c-9520-8ae56a51bb4c in /on_select and /on_confirm
- store name  /fulfillments[0]/start/location/descriptor/name can't change
- Discrepancies between the quote object /on_select and /on_confirm

**/status**
-  must have required property 'context'
-  must have required property 'message'

**/update**
- /message/order/items/0/tags/ttl_approval must match format "duration"