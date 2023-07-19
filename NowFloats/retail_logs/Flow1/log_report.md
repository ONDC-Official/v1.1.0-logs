**/on_search**
- /message/catalog/bpp~1providers/0/items/0/descriptor/images must NOT have more than 3 items
- /message/catalog/bpp~1providers/0/items/1/descriptor/images must NOT have more than 3 items
- /message/catalog/bpp~1providers/1/items/0/descriptor/images must NOT have more than 3 items
- /message/catalog/bpp~1providers/1/items/1/descriptor/images must NOT have more than 3 items
- /message/catalog/bpp~1providers/1/items/2/descriptor/images must NOT have more than 3 items
- /message/catalog/bpp~1providers/1/items/3/descriptor/images must NOT have more than 3 items
- /message/catalog/bpp~1providers/1/items/4/descriptor/images must NOT have more than 3 items

**/init**
- billing/created_at should match context.timestamp
- billing/updated_at should match context.timestamp
- value of address.name, address.building and address.locality should be unique

**/confirm**
- payment settlement_details mismatch in /on_init & /confirm
- order.created_at timestamp should match context.timestamp
- Discrepancies between the quote object in /on_select and /confirm

**/on_confirm**
- Discrepancies between the quote object /on_select and /on_confirm

**/on_status (Order-picked-up)**
- /fulfillments/0/end/time delivery time should not be present until order is delivered


**/update**
- /message/order/items/0/tags/ttl_approval must match format "duration"
- Timestamp for /on_confirm api cannot be greater than or equal to /update api


**/on_update (Return_Approved)**
- /fulfillments/1/state/descriptor/code must be equal to one of the allowed values (Pending,Packed,Order-picked-up,Out-for-delivery,Order-delivered,RTO-Initiated,RTO-Delivered,RTO-Disposed,Cancelled)
- message_id of all unsolicited /on_update calls should be same for a particular /update request




