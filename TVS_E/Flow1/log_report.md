**/on_search**
- /message/catalog/bpp~1providers/0/@ondc~1org~1fssai_license_no must NOT have fewer than 14 characters
- /message/catalog/bpp~1providers/0/items/0/descriptor must have required property 'symbol'
- /message/catalog/bpp~1providers/0/items/0/@ondc~1org~1statutory_reqs_packaged_commodities must have required property 'imported_product_country_of_origin'
- /message/catalog/bpp~1providers/0/items/1/descriptor must have required property 'symbol'
- /message/catalog/bpp~1providers/0/items/1/@ondc~1org~1statutory_reqs_packaged_commodities must have required property 'imported_product_country_of_origin'
- /message/catalog/bpp~1providers/0/items/2/descriptor must have required property 'symbol'
- /message/catalog/bpp~1providers/0/items/2/@ondc~1org~1statutory_reqs_packaged_commodities must have required property 'imported_product_country_of_origin'
- /message/catalog/bpp~1providers/0/fulfillments/0/contact/phone must NOT have fewer than 10 characters
- context/timestamp difference between /on_search and /search should be smaller than 5 sec
- Either one of fixed (range) or split (frequency and times) timings should be provided in /bpp/providers[0]/locations[0]/time
- available count of item should be smaller or equal to the maximum count (/bpp/providers[0]/items[0]/quantity)
- @ondc/org/contact_details_consumer_care should be in the format "name,email,contactno" in /bpp/providers[0]/items
- available count of item should be smaller or equal to the maximum count (/bpp/providers[0]/items[1]/quantity)
- available count of item should be smaller or equal to the maximum count (/bpp/providers[0]/items[2]/quantity)
- category in serviceability construct should be one of the category ids bpp/providers[0]/items/category_id

**/select**
- Timestamp for /on_search api cannot be greater than or equal to /select api

**/on_select**
- /quote/breakup/0 must have required property '@ondc/org/title_type'
- /quote/breakup/0 must have required property '@ondc/org/item_id'
- /quote/breakup/1 must have required property '@ondc/org/title_type'
- /quote/breakup/1 must have required property '@ondc/org/item_id'
- /quote/breakup/2 must have required property '@ondc/org/title_type'
- /quote/breakup/2 must have required property '@ondc/org/item_id'
- /quote/breakup/3 must have required property '@ondc/org/title_type'
- /quote/breakup/3 must have required property '@ondc/org/item_id'
- /fulfillments/0 must have required property '@ondc/org/provider_name'
- /fulfillments/0 must have required property '@ondc/org/category'
- /fulfillments/0/state/descriptor must have required property 'code'
- City code mismatch in /search and /on_select
- context/timestamp difference between /on_select and /select should be smaller than 5 sec
- /fulfillments[0]/@ondc/org/TAT (O2D) in /on_select can't be smaller than @ondc/org/time_ship (O2S) in /on_search
- Pre-order fulfillment state codes should be used in fulfillments[].state.descriptor.code
- Warning: Quoted Price in /on_select INR 0 does not match with the total price of items in /select INR 27608
- delivery line item must be present in quote/breakup (if location is serviceable)
- Quote breakup Payment title type "undefined" is not as per the API contract
- Quote breakup Payment title "Delivery Charge" is not as per the API Contract
- Quote breakup Payment title "Tax" comes under the title type "tax"

**/init**
- /message/order/billing/address must have required property 'building'
- /message/order/fulfillments/0/end/location/address/building must NOT have fewer than 3 characters
- Timestamp for  /on_select api cannot be greater than or equal to /init api
- address.building should be more than 3 chars

**/on_init**
- /items/0 must have required property 'fulfillment_id'
- /items/1 must have required property 'fulfillment_id'
- /billing must have required property 'created_at'
- /billing must have required property 'updated_at'
- /billing/address must have required property 'building'
- /billing/address must have required property 'locality'
- /fulfillments/0/end/location/address must have required property 'building'
- /fulfillments/0/end/location/address must have required property 'locality'
- /quote/breakup/0/@ondc~1org~1title_type must be equal to one of the allowed values (item,delivery,packing,tax,misc,discount)
- /quote/breakup/1/@ondc~1org~1title_type must be equal to one of the allowed values (item,delivery,packing,tax,misc,discount)
- /payment/@ondc~1org~1settlement_details/0/settlement_type must be equal to one of the allowed values (upi,neft,rtgs)
- City code mismatch in search & on_init
- context/timestamp difference between /on_init and /init should be smaller than 5 sec
- provider_location.id mismatches in /on_search and /on_init
- items[0].fulfillment_id mismatches for Item ba3ca63c-927e-4ca3-8694-19e2c7b32911 in /on_select and /on_init
- items[1].fulfillment_id mismatches for Item ba3ca63c-927e-4ca3-8694-19e2c7b32912 in /on_select and /on_init
- address/locality, created_at, updated_at mismatches in /billing in /init and /on_init
- Discrepancies between the quote object in /on_select and /on_init

**/confirm**
- /message/order/billing must have required property 'created_at'
- /message/order/billing must have required property 'updated_at'
- /message/order/billing/address must have required property 'building'
- /message/order/billing/address must have required property 'locality'
- /message/order/fulfillments/0/end/location/address must have required property 'building'
- /message/order/fulfillments/0/end/location/address must have required property 'locality'
- /message/order/quote/breakup/0/@ondc~1org~1title_type must be equal to one of the allowed values (item,delivery,packing,tax,misc,discount)
- /message/order/quote/breakup/1/@ondc~1org~1title_type must be equal to one of the allowed values (item,delivery,packing,tax,misc,discount)
- /message/order/payment/@ondc~1org~1settlement_details/0/settlement_type must be equal to one of the allowed values (upi,neft,rtgs)
- Timestamp for /on_init api cannot be greater than or equal to /confirm api
- provider.locations[0].id mismatches in /on_search and /confirm
- address/locality, created_at, updated_at mismatches in /billing in /init and /confirm
- Discrepancies between the quote object in /on_select and /confirm

**/on_confirm**
-  must have required property 'created_at'
-  must have required property 'updated_at'
- /items/0 must have required property 'fulfillment_id'
- /items/1 must have required property 'fulfillment_id'
- /billing must have required property 'created_at'
- /billing must have required property 'updated_at'
- /billing/address must have required property 'building'
- /billing/address must have required property 'locality'
- /fulfillments/0/state/descriptor/code must be equal to constant (Pending)
- /fulfillments/0/start must have required property 'contact'
- /fulfillments/0/start/location must have required property 'id'
- /fulfillments/0/start/location must have required property 'descriptor'
- /fulfillments/0/end/location/address must have required property 'building'
- /fulfillments/0/end/location/address must have required property 'locality'
- /quote must have required property 'ttl'
- /payment/params must have required property 'transaction_id'
- /payment/@ondc~1org~1buyer_app_finder_fee_type must be equal to one of the allowed values (percent,amount)
- /payment/@ondc~1org~1settlement_details/0/settlement_type must be equal to one of the allowed values (upi,neft,rtgs)
- City code mismatch in /search and /on_confirm
- context/timestamp difference between /on_confirm and /confirm should be smaller than 5 sec
- order.created_at timestamp mismatches in /confirm and /on_confirm
- order.updated_at timestamp should be updated as per the context.timestamp (since default fulfillment state is added)
- provider.locations[0].id mismatches in /on_search and /on_confirm
- items[0].fulfillment_id mismatches for Item ba3ca63c-927e-4ca3-8694-19e2c7b32911 in /on_select and /on_confirm
- items[1].fulfillment_id mismatches for Item ba3ca63c-927e-4ca3-8694-19e2c7b32912 in /on_select and /on_confirm
- address/door, address/street mismatches in /billing in /confirm and /on_confirm
- default fulfillments state is missing in /on_confirm
- Discrepancies between the quote object /on_select and /on_confirm
- Quoted Price in /on_confirm 29700.37 does not match with the quoted price in /on_select 27658.00
- payment object mismatches in /confirm & /on_confirm

**/cancel**
- City code mismatch in /select and /cancel
- Timestamp for /on_confirm api cannot be greater than or equal to /cancel api
- Transaction Id for should be same from /select onwards
- Order Id in /cancel and /confirm do not match

**/on_cancel**
- City code mismatch in /search and /on_cancel
- Timestamp for /on_confirm api cannot be greater than or equal to /on_cancel api
- Transaction Id should be same from /select onwards
- Order id in /on_cancel and /confirm do not match

**/track**
- City code mismatch in /search and /track
- Timestamp for /on_confirm api cannot be greater than or equal to /track api

**/on_track**
- City code mismatch in /search and /on_track

**/status**
- City code mismatch in /search and /status
- Timestamp for /on_confirm api cannot be greater than or equal to /status api

**/on_status (Pending)**
-  must have required property 'documents'
-  must have required property 'created_at'
-  must have required property 'updated_at'
- /items/0 must have required property 'fulfillment_id'
- /items/1 must have required property 'fulfillment_id'
- /billing must have required property 'created_at'
- /billing must have required property 'updated_at'
- /billing/address must have required property 'building'
- /billing/address must have required property 'locality'
- /fulfillments/0 must have required property '@ondc/org/provider_name'
- /fulfillments/0 must have required property 'state'
- /fulfillments/0/start must have required property 'contact'
- /fulfillments/0/end must have required property 'time'
- /fulfillments/0/end/location/address must have required property 'building'
- /fulfillments/0/end/location/address must have required property 'locality'
- /quote must have required property 'ttl'
- /payment must have required property '@ondc/org/buyer_app_finder_fee_type'
- /payment must have required property '@ondc/org/buyer_app_finder_fee_amount'
- /payment/params must have required property 'transaction_id'
- /payment/@ondc~1org~1settlement_details/0/settlement_type must be equal to one of the allowed values (upi,neft,rtgs)
- /payment/@ondc~1org~1settlement_details/0/settlement_counterparty must be equal to constant (buyer)
- /payment/@ondc~1org~1settlement_details/0/settlement_phase must be equal to constant (refund)
- /payment/@ondc~1org~1settlement_details/0/settlement_type must be equal to one of the allowed values (upi,neft,rtgs)
- City code mismatch in search and /on_status_pending
- address/door, address/street mismatches in /billing in /confirm and /on_status_pending
- provider.locations[0].id mismatches in /on_search and /on_status_pending
- order/created_at timestamp can't change (should remain same as in /confirm)
-  order.updated_at timestamp should match context timestamp for /on_status_pending api

**/on_status (Order-picked-up)**
-  must have required property 'documents'
-  must have required property 'created_at'
-  must have required property 'updated_at'
- /items/0 must have required property 'fulfillment_id'
- /items/1 must have required property 'fulfillment_id'
- /billing must have required property 'created_at'
- /billing must have required property 'updated_at'
- /billing/address must have required property 'building'
- /billing/address must have required property 'locality'
- /fulfillments/0 must have required property '@ondc/org/provider_name'
- /fulfillments/0/start must have required property 'contact'
- /fulfillments/0/end must have required property 'time'
- /fulfillments/0/end/location/address must have required property 'building'
- /fulfillments/0/end/location/address must have required property 'locality'
- /quote must have required property 'ttl'
- /payment must have required property '@ondc/org/buyer_app_finder_fee_type'
- /payment must have required property '@ondc/org/buyer_app_finder_fee_amount'
- /payment/params must have required property 'transaction_id'
- /payment/@ondc~1org~1settlement_details/0/settlement_type must be equal to one of the allowed values (upi,neft,rtgs)
- /payment/@ondc~1org~1settlement_details/0/settlement_counterparty must be equal to constant (buyer)
- /payment/@ondc~1org~1settlement_details/0/settlement_phase must be equal to constant (refund)
- /payment/@ondc~1org~1settlement_details/0/settlement_type must be equal to one of the allowed values (upi,neft,rtgs)
- City code mismatch in search and /on_status_picked
- Message Id cannot be same for different sets of APIs
- address/door, address/street mismatches in /billing in /confirm and /on_status_picked
- provider.locations[0].id mismatches in /on_search and /on_status_picked
- order/created_at timestamp can't change (should remain same as in /confirm)
- order/state should be "In-progress" for /on_status_picked
- pickup timestamp should match context/timestamp and can't be future dated
- order/updated_at timestamp can't be less than the pickup time
- order/updated_at timestamp can't be future dated (should match context/timestamp)

**/on_status (Order-Delivered)**
-  must have required property 'documents'
-  must have required property 'created_at'
-  must have required property 'updated_at'
- /items/0 must have required property 'fulfillment_id'
- /items/1 must have required property 'fulfillment_id'
- /billing must have required property 'created_at'
- /billing must have required property 'updated_at'
- /billing/address must have required property 'building'
- /billing/address must have required property 'locality'
- /fulfillments/0 must have required property '@ondc/org/provider_name'
- /fulfillments/0/start must have required property 'contact'
- /fulfillments/0/end/location/address must have required property 'building'
- /fulfillments/0/end/location/address must have required property 'locality'
- /quote must have required property 'ttl'
- /payment must have required property '@ondc/org/buyer_app_finder_fee_type'
- /payment must have required property '@ondc/org/buyer_app_finder_fee_amount'
- /payment/params must have required property 'transaction_id'
- /payment/@ondc~1org~1settlement_details/0/settlement_type must be equal to one of the allowed values (upi,neft,rtgs)
- /payment/@ondc~1org~1settlement_details/0/settlement_counterparty must be equal to constant (buyer)
- /payment/@ondc~1org~1settlement_details/0/settlement_phase must be equal to constant (refund)
- /payment/@ondc~1org~1settlement_details/0/settlement_type must be equal to one of the allowed values (upi,neft,rtgs)
- City code mismatch in search and /on_status_delivered
- Message Id cannot be same for different sets of APIs
- address/door, address/street mismatches in /billing in /confirm and /on_status_delivered
- order/created_at timestamp can't change (should remain same as in /confirm)
- order/state should be "Completed" for /on_status_delivered
- delivery timestamp should match context/timestamp and can't be future dated
- delivery timestamp (/end/time/timestamp) can't be less than or equal to the pickup timestamp (start/time/timestamp)
- pickup time (/start/time/timestamp) can't change (should remain same as in "Order-picked-up" state) 
- order/updated_at timestamp can't be less than the delivery time
- order/updated_at timestamp can't be future dated (should match context/timestamp)

**/update**
- City code mismatch in /search and /update
- Timestamp for /on_confirm api cannot be greater than or equal to /update api

**/on_update (Initiated)**
-  must have required property 'payment'
- /items/0 must have required property 'fulfillment_id'
- /items/1 must have required property 'fulfillment_id'
- /fulfillments/0 must have required property 'id'
- /fulfillments/0 must have required property 'state'
- /fulfillments/0/start/location must have required property 'descriptor'
- /fulfillments/0/end/location/address must have required property 'building'
- /fulfillments/0/end/location/address must have required property 'locality'
- /quote must have required property 'ttl'
- City code mismatch in /search and /on_update_Return_Initiated
- quote price should not change for return state Return_Initiated
- new fulfillment id should not be created for item: ba3ca63c-927e-4ca3-8694-19e2c7b32911 when return state is Return_Initiated
- pickup timestamp (/start/time/timestamp) can't change for fulfillment id undefined
- delivery timestamp (/end/time/timestamp) can't change for fulfillment id undefined
- order/created_at timestamp can't change (should remain same as in /confirm)
- order created_at timestamp must always be earlier than the updated_at timestamp

**/on_update (Liquidated)**
-  must have required property 'payment'
- /items/0 must have required property 'fulfillment_id'
- /items/1 must have required property 'fulfillment_id'
- /fulfillments/0 must have required property 'id'
- /fulfillments/0 must have required property 'state'
- /fulfillments/0/start/location must have required property 'descriptor'
- /fulfillments/0/end/location/address must have required property 'building'
- /fulfillments/0/end/location/address must have required property 'locality'
- /quote must have required property 'ttl'
- City code mismatch in /search and /on_update_Liquidated
- message_id of all unsolicited /on_update calls should be same for a particular /update request
- item quantity should be updated in quote/breakup for item: ba3ca63c-927e-4ca3-8694-19e2c7b32912 when state is Liquidated
- item quantity should be updated in quote/breakup for item: ba3ca63c-927e-4ca3-8694-19e2c7b32911 when state is Liquidated
- return state should be Liquidated in /items/tags/status for item: ba3ca63c-927e-4ca3-8694-19e2c7b32912
- new fulfillment id should not be created for item: ba3ca63c-927e-4ca3-8694-19e2c7b32911 when return state is Liquidated
- pickup timestamp (/start/time/timestamp) can't change for fulfillment id undefined
- delivery timestamp (/end/time/timestamp) can't change for fulfillment id undefined
- order/created_at timestamp can't change (should remain same as in /confirm)
- order created_at timestamp must always be earlier than the updated_at timestamp

**/on_update (Rejected)**
-  must have required property 'payment'
- /items/0 must have required property 'fulfillment_id'
- /items/1 must have required property 'fulfillment_id'
- /fulfillments/0 must have required property 'id'
- /fulfillments/0 must have required property 'state'
- /fulfillments/0/start/location must have required property 'descriptor'
- /fulfillments/0/end/location/address must have required property 'building'
- /fulfillments/0/end/location/address must have required property 'locality'
- /quote must have required property 'ttl'
- City code mismatch in /search and /on_update_Return_Rejected
- message_id of all unsolicited /on_update calls should be same for a particular /update request
- quote price should not change for return state Return_Rejected
- new fulfillment id should not be created for item: ba3ca63c-927e-4ca3-8694-19e2c7b32911 when return state is Return_Rejected
- return state should be Return_Rejected in /items/tags/status for item: ba3ca63c-927e-4ca3-8694-19e2c7b32911
- pickup timestamp (/start/time/timestamp) can't change for fulfillment id undefined
- delivery timestamp (/end/time/timestamp) can't change for fulfillment id undefined
- order/created_at timestamp can't change (should remain same as in /confirm)
- order created_at timestamp must always be earlier than the updated_at timestamp

**/on_update (Return_Approved)**
-  must have required property 'created_at'
-  must have required property 'updated_at'
- /items/0 must have required property 'fulfillment_id'
- /items/1 must have required property 'fulfillment_id'
- /fulfillments/0/state/descriptor/code must be equal to one of the allowed values (Pending,Packed,Order-picked-up,Out-for-delivery,Order-delivered,RTO-Initiated,RTO-Delivered,RTO-Disposed,Cancelled)
- /fulfillments/0/end/location/address must have required property 'building'
- /fulfillments/0/end/location/address must have required property 'locality'
- /quote must have required property 'ttl'
- /payment must have required property '@ondc/org/buyer_app_finder_fee_type'
- /payment must have required property '@ondc/org/buyer_app_finder_fee_amount'
- /payment/params must have required property 'transaction_id'
- /payment/@ondc~1org~1settlement_details/0/settlement_type must be equal to one of the allowed values (upi,neft,rtgs)
- /payment/@ondc~1org~1settlement_details/0/settlement_counterparty must be equal to constant (buyer)
- /payment/@ondc~1org~1settlement_details/0/settlement_phase must be equal to constant (refund)
- /payment/@ondc~1org~1settlement_details/0/settlement_type must be equal to one of the allowed values (upi,neft,rtgs)
- context.action should be on_update
- City code mismatch in /search and /on_update_Return_Approved
- message_id of all unsolicited /on_update calls should be same for a particular /update request
- quote price should not change for return state Return_Approved
- return state must be present in /items/tags for item: ba3ca63c-927e-4ca3-8694-19e2c7b32912
- item with id: ba3ca63c-927e-4ca3-8694-19e2c7b32911 can't be returned when order is not delivered (fulfillment state should be Order-delivered)
- return state must be present in /items/tags for item: ba3ca63c-927e-4ca3-8694-19e2c7b32911
- Reverse QC fulfillment should be created for return state Return_Approved
- pickup timestamp (/start/time/timestamp) can't change for fulfillment id 1
- delivery timestamp (/end/time/timestamp) can't change for fulfillment id 1
- order/updated_at timestamp can't be future dated (should match context/timestamp)
- order/created_at timestamp can't change (should remain same as in /confirm)
- item with id: Tax in quote.breakup[2] does not exist in items[] (should be valid item id)
- invalid  id: Delivery in delivery line item (should be a valid fulfillment_id)
- quote.price.value 31869.39 does not match with the price breakup 29700.37

**/on_update (Return_Picked)**
-  must have required property 'payment'
- /items/0 must have required property 'fulfillment_id'
- /items/1 must have required property 'fulfillment_id'
- /fulfillments/0 must have required property 'id'
- /fulfillments/0/state/descriptor/code must be equal to one of the allowed values (Pending,Packed,Order-picked-up,Out-for-delivery,Order-delivered,RTO-Initiated,RTO-Delivered,RTO-Disposed,Cancelled)
- /fulfillments/0/start/location must have required property 'descriptor'
- /fulfillments/0/end/location/address must have required property 'building'
- /fulfillments/0/end/location/address must have required property 'locality'
- /quote must have required property 'ttl'
- City code mismatch in /search and /on_update_Return_Picked
- message_id of all unsolicited /on_update calls should be same for a particular /update request
- item quantity should be updated in quote/breakup for item: ba3ca63c-927e-4ca3-8694-19e2c7b32912 when state is Return_Picked
- item quantity should be updated in quote/breakup for item: ba3ca63c-927e-4ca3-8694-19e2c7b32911 when state is Return_Picked
- return state should be Return_Picked in /items/tags/status for item: ba3ca63c-927e-4ca3-8694-19e2c7b32912
- Reverse QC fulfillment should be created for return state Return_Picked
- pickup timestamp (/start/time/timestamp) can't change for fulfillment id undefined
- delivery timestamp (/end/time/timestamp) can't change for fulfillment id undefined
- order/created_at timestamp can't change (should remain same as in /confirm)
- order created_at timestamp must always be earlier than the updated_at timestamp
- fulfillments/state should be "Order-picked-up" for /on_status_Return_Picked

**/on_update (Return_Delivered)**
-  must have required property 'payment'
- /items/0 must have required property 'fulfillment_id'
- /items/1 must have required property 'fulfillment_id'
- /fulfillments/0 must have required property 'id'
- /fulfillments/0/state/descriptor/code must be equal to one of the allowed values (Pending,Packed,Order-picked-up,Out-for-delivery,Order-delivered,RTO-Initiated,RTO-Delivered,RTO-Disposed,Cancelled)
- /fulfillments/0/start/location must have required property 'descriptor'
- /fulfillments/0/end/location/address must have required property 'building'
- /fulfillments/0/end/location/address must have required property 'locality'
- /quote must have required property 'ttl'
- City code mismatch in /search and /on_update_Return_Delivered
- message_id of all unsolicited /on_update calls should be same for a particular /update request
- item quantity should be updated in quote/breakup for item: ba3ca63c-927e-4ca3-8694-19e2c7b32912 when state is Return_Delivered
- item quantity should be updated in quote/breakup for item: ba3ca63c-927e-4ca3-8694-19e2c7b32911 when state is Return_Delivered
- return state should be Return_Delivered in /items/tags/status for item: ba3ca63c-927e-4ca3-8694-19e2c7b32912
- Reverse QC fulfillment should be created for return state Return_Delivered
- pickup timestamp (/start/time/timestamp) can't change for fulfillment id undefined
- delivery timestamp (/end/time/timestamp) can't change for fulfillment id undefined
- order/created_at timestamp can't change (should remain same as in /confirm)
- order created_at timestamp must always be earlier than the updated_at timestamp
- fulfillments/state should be "Order-delivered" for /on_update_Return_Delivered
- 

