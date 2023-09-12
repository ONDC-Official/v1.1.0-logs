**/search**
- /message/intent/payment/@ondc~1org~1buyer_app_finder_fee_type must be equal to constant (percent)

**/on_select**
- tax line item should not be present if price=0
- discount line item should not be present if price=0

**/init**
- /message/order/items/1 must have required property 'fulfillment_id'
- items[1].fulfillment_id mismatches for Item Proteus18TH10002 in /on_select and /init

**/on_init**
- /quote/breakup/3/price/value must be string
- /quote/breakup/4/price/value must match pattern "^(\d*.?\d{1,2})$"
- Quoted Price 1401.22 does not match with Net Breakup Price 1401.2199999999998 in /on_init
- Quoted Price in /on_init INR 1401.22 does not match with the quoted price in /on_select INR 1398
- Discrepancies between the quote object in /on_select and /on_init

**/confirm**
- /message/order/items/1 must have required property 'fulfillment_id'
- /message/order/quote/breakup/3/price/value must be string
- /message/order/quote/breakup/4/price/value must match pattern "^(\d*.?\d{1,2})$"
- /message/order/payment/status must be equal to constant (PAID)
- /message/order/payment/type must be equal to constant (ON-ORDER)
- /message/order/payment/collected_by must be equal to constant (BAP)
- /message/order/payment/@ondc~1org~1buyer_app_finder_fee_type must be equal to one of the allowed values (percent,amount)
- items[1].fulfillment_id mismatches for Item Proteus18TH10002 in /on_select and /confirm
- address/door mismatches in /billing in /init and /confirm
- Discrepancies between the quote object in /on_select and /confirm
- Quoted Price in /confirm INR 1401.22 does not match with the quoted price in /on_select INR 1398

**/on_confirm**
- /fulfillments/0 must have required property '@ondc/org/provider_name'
- /fulfillments/0/start must have required property 'contact'
- /quote/breakup/4/price/value must match pattern "^(\d*.?\d{1,2})$"
- /payment/status must be equal to constant (PAID)
- /payment/type must be equal to constant (ON-ORDER)
- /payment/collected_by must be equal to constant (BAP)
- /payment/@ondc~1org~1buyer_app_finder_fee_type must be equal to one of the allowed values (percent,amount)
- order.created_at timestamp mismatches in /confirm and /on_confirm
- created_at, updated_at mismatches in /billing in /confirm and /on_confirm
- store gps location /fulfillments[0]/start/location/gps can't change
- store name  /fulfillments[0]/start/location/descriptor/name can't change
- Discrepancies between the quote object /on_select and /on_confirm
- Quoted Price in /on_confirm 1401.22 does not match with the quoted price in /on_select 1398

