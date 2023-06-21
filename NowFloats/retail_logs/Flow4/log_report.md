**/on_search**
- /message/catalog/bpp~1providers/0/items/0/descriptor/images must NOT have more than 3 items
- /bpp/providers[0]/locations[0]/gps coordinates must be specified with at least six decimal places of precision.
- Either one of fixed (range) or split (frequency and times) timings should be provided in /bpp/providers[0]/locations[0]/time
- location in serviceability construct should be one of the location ids bpp/providers[0]/locations
- category in serviceability construct should be one of the category ids bpp/providers[0]/items/category_id

**/select**
- Item Id 66d697f7-2937-475c-9520-8ae56a51bb4c does not exist in /on_search

**/on_select**
- /fulfillments/0/state/descriptor/code must be equal to one of the allowed values (Serviceable,Non-serviceable)
- /fulfillments[0]/@ondc/org/TAT (O2D) in /on_select can't be smaller than @ondc/org/time_ship (O2S) in /on_search
- Pre-order fulfillment state codes should be used in fulfillments[].state.descriptor.code
- item with id: 66d697f7-2937-475c-9520-8ae56a51bb4c is not present in /on_search

**/init**
- /message/order/billing/address must have required property 'building'
- /message/order/fulfillments/0/end/location/address/name must NOT have fewer than 3 characters
- /message/order/fulfillments/0/end/location/address/building must NOT have fewer than 3 characters
- /message/order/fulfillments/0/end/location/address/locality must NOT have fewer than 3 characters
- billing/created_at should match context.timestamp
- billing/updated_at should match context.timestamp
- address.building should be more than 3 chars
- address.name should be more than 3 chars
- address.locality should be more than 3 chars

**/on_init**
- /billing/address must have required property 'building'
- /payment/@ondc~1org~1settlement_details/0 must have required property 'bank_name'
- /payment/@ondc~1org~1settlement_details/0 must have required property 'branch_name'
- Discrepancies between the quote object in /on_select and /on_init

**/confirm**
- /message/order/billing/address must have required property 'building'
- /message/order/payment/status must be equal to constant (PAID)
- /message/order/payment/type must be equal to constant (ON-ORDER)
- /message/order/payment/collected_by must be equal to constant (BAP)
- /message/order/payment/@ondc~1org~1settlement_details/0 must have required property 'bank_name'
- /message/order/payment/@ondc~1org~1settlement_details/0 must have required property 'branch_name'
- order.created_at timestamp should match context.timestamp
- Discrepancies between the quote object in /on_select and /confirm

**/on_confirm**
- /billing/address must have required property 'building'
- /fulfillments/0/end/location/address must have required property 'building'
- /payment/status must be equal to constant (PAID)
- /payment/type must be equal to constant (ON-ORDER)
- /payment/collected_by must be equal to constant (BAP)
- /payment/@ondc~1org~1settlement_details/0 must have required property 'bank_name'
- /payment/@ondc~1org~1settlement_details/0 must have required property 'branch_name'
- items[0].fulfillment_id mismatches for Item 66d697f7-2937-475c-9520-8ae56a51bb4c in /on_select and /on_confirm
- items[1].fulfillment_id mismatches for Item e9511f3c-4592-4d7b-b038-ae5b6b1a58e5 in /on_select and /on_confirm
- store gps location /fulfillments[0]/start/location/gps can't change
- store name  /fulfillments[0]/start/location/descriptor/name can't change
- Discrepancies between the quote object /on_select and /on_confirm

**/update**
- /message/order/items/0/tags/ttl_approval must match format "duration"

