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
    : IDENTIFIER COLON
    ;


normalInst
    : opCode COMMA operandList RIGHT_ARROW operandList // normal instruction.
    | operandList RIGHT_ARROW operandList // syntax sugar for mov.
    | opCode COMMA operandList // no dst operand.
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
    | label
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
    ;



