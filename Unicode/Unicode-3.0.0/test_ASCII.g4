/** 
test_ASCII.g4
Sample grammar for comparison.
 */ 

grammar      test_ASCII;



prog   : hello * EOF
;

hello  : 'hello' ID
;

/* in test_Codepoint.g4 ID and WS will be provided by classify.g4 */

ID     : [A-Za-z_] +           ;

WS     : [ \t\r\n] + -> skip   ;

ErrorCharacter : . ;
