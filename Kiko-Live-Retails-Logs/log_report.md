**/on_search**
- /message/catalog/bpp~1providers/0/items/0/@ondc~1org~1statutory_reqs_packaged_commodities must be object
- /message/catalog/bpp~1providers/0/items/0/@ondc~1org~1time_to_ship must match format "duration"
- /message/catalog/bpp~1providers/0/items/0/@ondc~1org~1statutory_reqs_prepackaged_food must be object
- /message/catalog/bpp~1providers/0/items/0/@ondc~1org~1statutory_reqs_packaged_commodities must be object

**/select**
- Item Id 64afa8b8682cee3b504c4ac7 does not exist in /on_search

**/on_select**
- /quote/price/value must match pattern "^(\d*.?\d{1,2})$"
- /quote/breakup/5/price/value must match pattern "^(\d*.?\d{1,2})$"
- context/timestamp difference between /on_select and /select should be smaller than 5 sec
- item with id: 64afa8b8682cee3b504c4ac7 is not present in /on_search
- Item's unit and total price mismatch for id: 64afa8b8682cee3b504c4ac7
- item with id: fulfillment-64afa47e682cee3b504c4a86 in quote.breakup[4] does not exist in items[] (should be a valid item id)
- quote.price.value 383.098 does not match with the price breakup 383.10
- Warning: Quoted Price in /on_select INR 190 does not match with the total price of items in /select INR 200

**/init**
- /message/order/billing/address must have required property 'building'
- /message/order/fulfillments/0/end/location/address/building must NOT have fewer than 3 characters
- Timestamp for  /on_select api cannot be greater than or equal to /init api
- address.building should be more than 3 chars

**/on_init**
- /billing/address must have required property 'building'
- /quote/price/value must match pattern "^(\d*.?\d{1,2})$"
- /quote/breakup/5/price/value must match pattern "^(\d*.?\d{1,2})$"

**/confirm**
- /message/order/billing/address must have required property 'building'
- /message/order/quote/price/value must match pattern "^(\d*.?\d{1,2})$"
- /message/order/quote/breakup/5/price/value must match pattern "^(\d*.?\d{1,2})$"
- /message/order/payment/params/amount must match pattern "^(\d*.?\d{1,2})$"
- created_at, updated_at mismatches in /billing in /init and /confirm

**/on_confirm**
- /billing/address must have required property 'building'
- /fulfillments/0/end/time/range/end must match format "date-time"
- /quote/price/value must match pattern "^(\d*.?\d{1,2})$"
- /quote/breakup/5/price/value must match pattern "^(\d*.?\d{1,2})$"
- /payment/params/amount must match pattern "^(\d*.?\d{1,2})$"
- context/timestamp difference between /on_confirm and /confirm should be smaller than 5 sec
- order.created_at timestamp mismatches in /confirm and /on_confirm
- created_at, updated_at mismatches in /billing in /confirm and /on_confirm
- store gps location /fulfillments[0]/start/location/gps can't change
- store name  /fulfillments[0]/start/location/descriptor/name can't change

**/status**
- Timestamp for /on_confirm api cannot be greater than or equal to /status api

**/on_status (Pending)**
- /billing/address must have required property 'building'
- /fulfillments/0/start/time pickup time is mandatory when order is picked and thereafter
- /quote/price/value must match pattern "^(\d*.?\d{1,2})$"
- /quote/breakup/5/price/value must match pattern "^(\d*.?\d{1,2})$"
- /payment/params/amount must match pattern "^(\d*.?\d{1,2})$"
- Timestamp for /on_confirm api cannot be greater than or equal to /on_status_pending api
- created_at, updated_at mismatches in /billing in /confirm and /on_status_pending
- order/created_at timestamp can't change (should remain same as in /confirm)
-  order.updated_at timestamp should match context timestamp for /on_status_pending api

**/on_status (Order-picked-up)**
-  Invoice url must be present as part of documents objects (only in Order-picked-up state and thereafter)
- /billing/address must have required property 'building'
- /fulfillments/0/end/time/range/end must match format "date-time"
- /quote/price/value must match pattern "^(\d*.?\d{1,2})$"
- /quote/breakup/5/price/value must match pattern "^(\d*.?\d{1,2})$"
- /payment/params/amount must match pattern "^(\d*.?\d{1,2})$"
- Timestamp for /on_confirm api cannot be greater than or equal to /on_status_picked api
- created_at, updated_at mismatches in /billing in /confirm and /on_status_picked
- order/created_at timestamp can't change (should remain same as in /confirm)
- order/state should be "In-progress" for /on_status_picked
- fulfillments/state should be Order-picked-up for /on_status_picked

**/on_status (Order-Delivered)**
- /billing/address must have required property 'building'
- /fulfillments/0/start/time pickup time is mandatory when order is picked and thereafter
- /fulfillments/0/end/time delivery time is mandatory when order is delivered
- /quote/price/value must match pattern "^(\d*.?\d{1,2})$"
- /quote/breakup/5/price/value must match pattern "^(\d*.?\d{1,2})$"
- /payment/params/amount must match pattern "^(\d*.?\d{1,2})$"
- created_at, updated_at mismatches in /billing in /confirm and /on_status_delivered
- order/created_at timestamp can't change (should remain same as in /confirm)
- delivery timestamp should match context/timestamp and can't be future dated
- order/updated_at timestamp can't be less than the delivery time

