#include<windows.h>

int main() {
    MessageBox(
        NULL,                       // No parent window
        "Hello, World!",            // Message text
        "My Message Box",           // Message box title
        MB_OK | MB_ICONINFORMATION   // Buttons and icon type
    );
    return 0;
}
