class Solution {
    public String convertToTitle(int n) {
        /*
            使用Hashmap来储存每个字母 0-25/a-z
        */
        HashMap<Integer, Character> map = new HashMap<>();
        for (int i = 0; i < 26; i++) {
            map.put(i, (char)(65+i));
        }

        /*
            使用StringBuilder来添加每个字母在开头
        */
        StringBuilder sb = new StringBuilder();
        while (n != 0) {
            sb.insert(0, map.get((n-1)%26));
            n = (n-1)/26;
        }
        return sb.toString();
    }
}