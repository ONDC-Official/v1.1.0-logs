**/on_search**
- /message/catalog/bpp~1providers/0/@ondc~1org~1fssai_license_no must NOT have fewer than 14 characters
- /message/catalog/bpp~1providers/0/items/0/descriptor must have required property 'symbol'
- /message/catalog/bpp~1providers/0/items/0/@ondc~1org~1statutory_reqs_packaged_commodities must have required property 'imported_product_country_of_origin'
- /message/catalog/bpp~1providers/0/items/1/descriptor must have required property 'symbol'
- /message/catalog/bpp~1providers/0/items/1/@ondc~1org~1statutory_reqs_packaged_commodities must have required property 'imported_product_country_of_origin'
- /message/catalog/bpp~1providers/0/items/2/descriptor must have required property 'symbol'
- /message/catalog/bpp~1providers/0/items/2/@ondc~1org~1statutory_reqs_packaged_commodities must have required property 'imported_product_country_of_origin'
- /message/catalog/bpp~1providers/0/items/3/descriptor must have required property 'symbol'
- /message/catalog/bpp~1providers/0/items/3/@ondc~1org~1statutory_reqs_packaged_commodities must have required property 'imported_product_country_of_origin'
- /message/catalog/bpp~1providers/0/fulfillments/0/contact/phone must NOT have fewer than 10 characters
- context/timestamp difference between /on_search and /search should be smaller than 5 sec
- Either one of fixed (range) or split (frequency and times) timings should be provided in /bpp/providers[0]/locations[0]/time
- @ondc/org/contact_details_consumer_care should be in the format "name,email,contactno" in /bpp/providers[0]/items
- available count of item should be smaller or equal to the maximum count (/bpp/providers[0]/items[2]/quantity)
- available count of item should be smaller or equal to the maximum count (/bpp/providers[0]/items[3]/quantity)

**/select**
- Timestamp for /on_search api cannot be greater than or equal to /select api

**/on_select**
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
- Item's unit and total price mismatch for id: ba3ca63c-927e-4ca3-8694-19e2c7b32912
- available count can't be greater than maximum count for item id: ba3ca63c-927e-4ca3-8694-19e2c7b32912
- Warning: Quoted Price in /on_select INR 21354.24 does not match with the total price of items in /select INR 55216
- delivery line item must be present in quote/breakup (if location is serviceable)
- Quote breakup Payment title type "undefined" is not as per the API contract
- Quote breakup Payment title "Tax" comes under the title type "tax"
- Quote breakup Payment title "Delivery Charge" is not as per the API Contract

**/init**
- /message/order/billing/address must have required property 'building'
- /message/order/fulfillments/0/end/location/address/building must NOT have fewer than 3 characters
- Timestamp for  /on_select api cannot be greater than or equal to /init api
- address.building should be more than 3 chars

**/on_init**
- /items/0 must have required property 'fulfillment_id'
- /billing must have required property 'created_at'
- /billing must have required property 'updated_at'
- /billing/address must have required property 'building'
- /billing/address must have required property 'locality'
- /fulfillments/0/end/location/address must have required property 'building'
- /fulfillments/0/end/location/address must have required property 'locality'
- /quote/breakup/0/@ondc~1org~1title_type must be equal to one of the allowed values (item,delivery,packing,tax,misc,discount)
- /payment/@ondc~1org~1settlement_details/0/settlement_type must be equal to one of the allowed values (upi,neft,rtgs)
- City code mismatch in search & on_init
- context/timestamp difference between /on_init and /init should be smaller than 5 sec
- provider_location.id mismatches in /on_search and /on_init
- items[0].fulfillment_id mismatches for Item ba3ca63c-927e-4ca3-8694-19e2c7b32912 in /on_select and /on_init
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
- /message/order/payment/@ondc~1org~1settlement_details/0/settlement_type must be equal to one of the allowed values (upi,neft,rtgs)
- Timestamp for /on_init api cannot be greater than or equal to /confirm api
- provider.locations[0].id mismatches in /on_search and /confirm
- address/locality, created_at, updated_at mismatches in /billing in /init and /confirm
- Discrepancies between the quote object in /on_select and /confirm

**/on_confirm**
-  must have required property 'created_at'
-  must have required property 'updated_at'
- /items/0 must have required property 'fulfillment_id'
- /billing must have required property 'created_at'
- /billing must have required property 'updated_at'
- /billing/address must have required property 'building'
- /billing/address must have required property 'locality'
- /fulfillments/0/state/descriptor/code must be equal to constant (Pending)
- /fulfillments/0/start must have required property 'contact'
- /fulfillments/0/start/location must have required property 'id'
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
- items[0].fulfillment_id mismatches for Item ba3ca63c-927e-4ca3-8694-19e2c7b32912 in /on_select and /on_confirm
- address/area_code, address/door, address/street mismatches in /billing in /confirm and /on_confirm
- default fulfillments state is missing in /on_confirm
- store name  /fulfillments[0]/start/location/descriptor/name can't change
- fulfillments[0].end.location.address.area_code is not matching with area_code in /select
- Discrepancies between the quote object /on_select and /on_confirm
- payment object mismatches in /confirm & /on_confirm

**/cancel**
- City code mismatch in /select and /cancel
- Timestamp for /on_confirm api cannot be greater than or equal to /cancel api

**/on_cancel**
- City code mismatch in /search and /on_cancel

