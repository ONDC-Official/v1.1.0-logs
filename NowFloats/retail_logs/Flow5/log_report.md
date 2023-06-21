**/on_search**
- /context/action must be equal to constant (on_search)
- /message must have required property 'catalog'
- context.action should be on_search
- context/timestamp difference between /on_search and /search should be smaller than 5 sec
- Message Id for /search and /on_search api should be same

**/select**
- Timestamp for /on_search api cannot be greater than or equal to /select api

**/on_select**
- /quote/breakup/2/price/value must match pattern "^(\d*.?\d{1,2})$"
- Message Id cannot be same for different sets of APIs
- provider.id mismatches in /on_search and /on_select

**/init**
- Provider Id mismatches in /select and /init
- Provider.locations[0].id mismatches in /select and /init
- billing/created_at should match context.timestamp
- billing/updated_at should match context.timestamp

**/on_init**
- /quote/breakup/2/price/value must match pattern "^(\d*.?\d{1,2})$"
- /payment/@ondc~1org~1settlement_details/0 must have required property 'bank_name'
- /payment/@ondc~1org~1settlement_details/0 must have required property 'branch_name'
- Provider Id mismatches in /on_search and /on_init
- provider_location.id mismatches in /on_search and /on_init
- Quoted Price in /on_init INR 90466.86 does not match with the quoted price in /on_select INR undefined
- Discrepancies between the quote object in /on_select and /on_init

**/confirm**
- /message/order/quote/breakup/2/price/value must match pattern "^(\d*.?\d{1,2})$"
- /message/order/payment/status must be equal to constant (PAID)
- /message/order/payment/type must be equal to constant (ON-ORDER)
- /message/order/payment/collected_by must be equal to constant (BAP)
- /message/order/payment/@ondc~1org~1settlement_details/0 must have required property 'bank_name'
- /message/order/payment/@ondc~1org~1settlement_details/0 must have required property 'branch_name'
- Provider Id mismatches in /on_search and /confirm
- provider.locations[0].id mismatches in /on_search and /confirm
- address/door mismatches in /billing in /init and /confirm
- order.created_at timestamp should match context.timestamp
- Discrepancies between the quote object in /on_select and /confirm
- Quoted Price in /confirm INR 90466.86 does not match with the quoted price in /on_select INR undefined

**/on_confirm**
- /quote/breakup/2/price/value must match pattern "^(\d*.?\d{1,2})$"
- /payment/status must be equal to constant (PAID)
- /payment/type must be equal to constant (ON-ORDER)
- /payment/collected_by must be equal to constant (BAP)
- /payment/@ondc~1org~1settlement_details/0 must have required property 'bank_name'
- /payment/@ondc~1org~1settlement_details/0 must have required property 'branch_name'
- Provider Id mismatches in /on_search and /on_confirm
- provider.locations[0].id mismatches in /on_search and /on_confirm
- items[0].fulfillment_id mismatches for Item f1207bbd-034f-4044-940c-67f4dc692c5c in /on_select and /on_confirm
- store name  /fulfillments[0]/start/location/descriptor/name can't change
- Discrepancies between the quote object /on_select and /on_confirm
- Quoted Price in /on_confirm 90466.86 does not match with the quoted price in /on_select undefined

