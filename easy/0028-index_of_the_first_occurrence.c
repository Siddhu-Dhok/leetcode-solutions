# Problem: 28. Index of the first occurrence
# Difficulty: Easy
# URL: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

// int strStr(char* haystack, char* needle) {
//     int flag = -1;
//     int size = sizeof(haystack)/sizeof(haystack[0]);
//     int size2 = sizeof(needle)/sizeof(needle[0]);
//     for (int i = 0; i < size; i++) {
//         if (haystack[i] == needle[0]) {
//             for(int j = 1; j < size2 - 1; j++){
//                 if (haystack[i + j] == needle[j]) {
//                     continue;
//                 }
//                 else break;
//                 flag = i;
//             }
//         }
//     }
//     return flag;
// }

#include <string.h>

int strStr(char* haystack, char* needle) {
    int size = strlen(haystack);
    int size2 = strlen(needle);

    if (size2 == 0) return 0;

    for (int i = 0; i <= size - size2; i++) {
        int j;
        for (j = 0; j < size2; j++) {
            if (haystack[i + j] != needle[j]) {
                break;
            }
        }
        if (j == size2) {
            return i;  // Found match
        }
    }
    return -1;  // No match found
}
