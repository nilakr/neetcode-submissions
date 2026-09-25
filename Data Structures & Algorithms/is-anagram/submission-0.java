class Solution {
    public boolean isAnagram(String s, String t) {
        HashSet<Character> sString = new HashSet<>();
        HashSet<Character> tString = new HashSet<>();

        for (int i = 0; i < s.length(); i++) {
            sString.add(s.charAt(i));
        }

        for (int i = 0; i < t.length(); i++) {
            tString.add(t.charAt(i));
        }

        if (sString.equals(tString)) {
            return true;
        }
        else {
            return false;
        }

    }
}
