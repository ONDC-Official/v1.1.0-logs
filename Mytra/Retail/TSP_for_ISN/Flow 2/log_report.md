**/search**
- /message/intent must have required property 'item'

**/on_search**
- context/timestamp difference between /on_search and /search should be smaller than 5 sec

**/on_select**
- context/timestamp difference between /on_select and /select should be smaller than 5 sec

**/init**
- City code mismatch in /search and /init

**/on_init**
- City code mismatch in search & on_init

**/confirm**
- City code mismatch in /search and /confirm
- address/door mismatches in /billing in /init and /confirm

**/on_confirm**
- City code mismatch in /search and /on_confirm
- context/timestamp difference between /on_confirm and /confirm should be smaller than 5 sec

**/on_cancel**
- City code mismatch in /search and /on_cancel

