**/on_select**
- tax line item should not be present if price=0
- discount line item should not be present if price=0
- Warning: Quoted Price in /on_select INR 499 does not match with the total price of items in /select INR 579

**/on_init**
- /quote/breakup/2/price/value must be string
- /quote/breakup/3/price/value must match pattern "^(\d*.?\d{1,2})$"
- Quoted Price in /on_init INR 513.01 does not match with the quoted price in /on_select INR 499
- Discrepancies between the quote object in /on_select and /on_init

**/confirm**
- /message/order/quote/breakup/2/price/value must be string
- /message/order/quote/breakup/3/price/value must match pattern "^(\d*.?\d{1,2})$"
- /message/order/payment/status must be equal to constant (PAID)
- /message/order/payment/type must be equal to constant (ON-ORDER)
- /message/order/payment/collected_by must be equal to constant (BAP)
- address/door mismatches in /billing in /init and /confirm
- Discrepancies between the quote object in /on_select and /confirm
- Quoted Price in /confirm INR 513.01 does not match with the quoted price in /on_select INR 499

**/on_confirm**
- /fulfillments/0 must have required property '@ondc/org/provider_name'
- /fulfillments/0/start must have required property 'contact'
- /quote/breakup/3/price/value must match pattern "^(\d*.?\d{1,2})$"
- /payment/status must be equal to constant (PAID)
- /payment/type must be equal to constant (ON-ORDER)
- /payment/collected_by must be equal to constant (BAP)
- order.created_at timestamp mismatches in /confirm and /on_confirm
- created_at, updated_at mismatches in /billing in /confirm and /on_confirm
- store gps location /fulfillments[0]/start/location/gps can't change
- store name  /fulfillments[0]/start/location/descriptor/name can't change
- Discrepancies between the quote object /on_select and /on_confirm
- Quoted Price in /on_confirm 513.01 does not match with the quoted price in /on_select 499

