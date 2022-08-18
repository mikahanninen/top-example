*** Settings ***
Library           TOTPLibrary    okta    code

*** Tasks ***
Get Okta Verification Code
    Log To Console    \nPrint OKTA codes in 5s intervals
    FOR    ${_}    IN RANGE    20
        ${code}=    Get TOTP
        Log To Console    Code: ${code}
        Sleep    5s
    END
