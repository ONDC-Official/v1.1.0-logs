**/on_search**
- /message/catalog/bpp~1providers/0/items/0/descriptor/images must NOT have more than 3 items

**/select**
- Item Id 66d697f7-2937-475c-9520-8ae56a51bb4c does not exist in /on_search

**/on_select**
- item with id: 66d697f7-2937-475c-9520-8ae56a51bb4c is not present in /on_search

**/init**
- billing/created_at should match context.timestamp
- billing/updated_at should match context.timestamp

**/on_init**
- Quoted Price in /on_init INR 5610.85 does not match with the quoted price in /on_select INR 7410.85
- Discrepancies between the quote object in /on_select and /on_init

**/confirm**
- address/door mismatches in /billing in /init and /confirm
- order.created_at timestamp should match context.timestamp
- Discrepancies between the quote object in /on_select and /confirm
- Quoted Price in /confirm INR 5610.85 does not match with the quoted price in /on_select INR 7410.85

**/on_confirm**
- items[0].fulfillment_id mismatches for Item e9511f3c-4592-4d7b-b038-ae5b6b1a58e5 in /on_select and /on_confirm
- items[1].fulfillment_id mismatches for Item 66d697f7-2937-475c-9520-8ae56a51bb4c in /on_select and /on_confirm
- store name  /fulfillments[0]/start/location/descriptor/name can't change
- Discrepancies between the quote object /on_select and /on_confirm
- Quoted Price in /on_confirm 5610.85 does not match with the quoted price in /on_select 7410.85

**/update**
- /message/order/items/0/tags/ttl_approval must match format "duration"

**/on_update (Initiated)**
-  must have required property 'payment'
-  must have required property 'created_at'
-  must have required property 'updated_at'
- /fulfillments/0/end must have required property 'time'
- /fulfillments/1/state/descriptor/code must be equal to one of the allowed values (Pending,Packed,Order-picked-up,Out-for-delivery,Order-delivered,RTO-Initiated,RTO-Delivered,RTO-Disposed,Cancelled)
- /fulfillments/1/end must have required property 'time'
- /quote/breakup/2/price/value must match pattern "^(\d*.?\d{1,2})$"
- returned item: e9511f3c-4592-4d7b-b038-ae5b6b1a58e5 should not be removed from quote when return state is Return_Initiated
- quote price should not change for return state Return_Initiated
- new fulfillment id should not be created for item: e9511f3c-4592-4d7b-b038-ae5b6b1a58e5 when return state is Return_Initiated
- Invalid quantity of items present in /order/items (returned & non-returned) for item: e9511f3c-4592-4d7b-b038-ae5b6b1a58e5
- order/created_at timestamp can't change (should remain same as in /confirm)
- item with id: 14a2e28f-be89-4a3f-9cc7-4688fe201a05 in quote.breakup[1] does not exist in items[]
- invalid  id: 7fd387fd-a5e7-41e7-8612-60ae39ceb6e5 in misc line item (should be a valid fulfillment_id)
- invalid  id: 7fd387fd-a5e7-41e7-8612-60ae39ceb6e5 in delivery line item (should be a valid fulfillment_id)

**/on_update (Return_Approved)**
-  must have required property 'payment'
-  must have required property 'created_at'
-  must have required property 'updated_at'
- /fulfillments/0/end must have required property 'time'
- /fulfillments/1/state/descriptor/code must be equal to one of the allowed values (Pending,Packed,Order-picked-up,Out-for-delivery,Order-delivered,RTO-Initiated,RTO-Delivered,RTO-Disposed,Cancelled)
- /fulfillments/1/end must have required property 'time'
- /fulfillments/2/state/descriptor/code must be equal to one of the allowed values (Pending,Packed,Order-picked-up,Out-for-delivery,Order-delivered,RTO-Initiated,RTO-Delivered,RTO-Disposed,Cancelled)
- /fulfillments/2/end must have required property 'time'
- /quote/breakup/2/price/value must match pattern "^(\d*.?\d{1,2})$"
- message_id of all unsolicited /on_update calls should be same for a particular /update request
- returned item: e9511f3c-4592-4d7b-b038-ae5b6b1a58e5 should not be removed from quote when return state is Return_Approved
- quote price should not change for return state Return_Approved
- new fulfillment id should be created for item: e9511f3c-4592-4d7b-b038-ae5b6b1a58e5 when return state is Return_Approved
- Invalid quantity of items present in /order/items (returned & non-returned) for item: e9511f3c-4592-4d7b-b038-ae5b6b1a58e5
- Reverse QC fulfillment should be created for return state Return_Approved
- order/created_at timestamp can't change (should remain same as in /confirm)
- item with id: 14a2e28f-be89-4a3f-9cc7-4688fe201a05 in quote.breakup[1] does not exist in items[]
- invalid  id: 7fd387fd-a5e7-41e7-8612-60ae39ceb6e5 in misc line item (should be a valid fulfillment_id)
- invalid  id: 7fd387fd-a5e7-41e7-8612-60ae39ceb6e5 in delivery line item (should be a valid fulfillment_id)

