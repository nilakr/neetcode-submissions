class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character, Integer> sString = new HashMap<>();
        HashMap<Character, Integer> tString = new HashMap<>();

        if (s.length() != t.length()) {
            return false;
        }

        for (int i = 0; i < s.length(); i++) {
            if (!sString.containsKey(s.charAt(i))) {
                sString.put(s.charAt(i), 1);
            }
            else {
                sString.put(s.charAt(i), sString.get(s.charAt(i)) + 1);
            }
        }

        for (int i = 0; i < t.length(); i++) {
            if (!tString.containsKey(t.charAt(i))) {
                tString.put(t.charAt(i), 1);
            }
            else {
                tString.put(t.charAt(i), tString.get(t.charAt(i)) + 1);
            }
        }

        if (sString.equals(tString)) {
            return true;
        }
        else {
            return false;
        }

    }
}
