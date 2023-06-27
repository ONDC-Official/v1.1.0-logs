**/on_select**
- context/timestamp difference between /on_select and /select should be smaller than 5 sec

**/on_init**
- context/timestamp difference between /on_init and /init should be smaller than 5 sec

**/on_update (Return_Approved)**
- /fulfillments/1/start/location must have required property 'descriptor'

**/on_update (Return_Delivered)**
- /fulfillments/1/start/location must have required property 'descriptor'
- quote.price.value 462.84 does not match with the price breakup 462.84000000000003

**/update (Refund)**
- Inaccurate calculation of refund amount (pls check the quote price in refund triggering state)

