parser grammar EasyCGRAParser;


options {
    tokenVocab = EasyCGRALexer;
}

compilationUnit 
    : entryBlock* EOF
    ;


entryBlock
    : entryHead LBRACE instList RBRACE
    ;

entryHead
    : ENTRY ENTRY_ARROW
    | ENTRY operandList ENTRY_ARROW
    ;

instList
    : inst*
    ;

inst
    : LBRACE normalInst* RBRACE
    | normalInst
    | label
    ;

label
    : labelID COLON
    ;

labelID
    : IDENTIFIER
    ;


normalInst
    : opCode COMMA operandList (RIGHT_ARROW operandList)?  // normal instruction.
    | operand RIGHT_ARROW operand // syntax sugar for mov. // no dst operand.
    ;

// operandList is like  [],[],[],[]
operandList
    : operand (COMMA operand)*
    ;

operand
    : predTag LBRACK idList RBRACK
    | IMM LBRACK DECIMAL_LITERAL RBRACK
    | IMM LBRACK OCT_LITERAL RBRACK
    | IMM LBRACK HEX_LITERAL RBRACK
    | IMM LBRACK BINARY_LITERAL RBRACK
    | IMM LBRACK FLOAT_LITERAL RBRACK
    | predTag MEM LBRACK idList RBRACK
    | predTag MEM LBRACK HEX_LITERAL RBRACK // MEM
    | labelID
    ;

idList
    : IDENTIFIER (COMMA IDENTIFIER)*
    ;

predTag
    : AND_PRED
    | OR_PRED
    | 
    ;


opCode
    : ADD
    | ADDI
    | SUB
    | SUBI
    | MUL
    | DIV
    | MAC
    | INC
    | LLS
    | LRS
    | OR
    | AND
    | XOR
    | NOT
    | FADD
    | FSUB
    | FMUL
    | FDIV
    | FMAC
    | MOV
    | MUL_CONST_ADD
    ;



