**/on_select**
- tax line item should not be present if price=0

**/on_update (Initiated)**
-  must have required property 'payment'
-  must have required property 'created_at'
-  must have required property 'updated_at'
- order/updated_at timestamp can't be future dated (should match context/timestamp)
- order/created_at timestamp can't change (should remain same as in /confirm)

**/on_update (Liquidated)**
-  must have required property 'payment'
-  must have required property 'created_at'
-  must have required property 'updated_at'
- order/updated_at timestamp can't be future dated (should match context/timestamp)
- order/created_at timestamp can't change (should remain same as in /confirm)

