import java.io.BufferedReader;
import java.io.InputStreamReader;

public class BOJ_2577 {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int A = Integer.parseInt(br.readLine());
        int B = Integer.parseInt(br.readLine());
        int C = Integer.parseInt(br.readLine());

        int res = A * B * C;
        String str = String.valueOf(res);
//        숫자 한 자리씩 다룰 때 문자열로 변환해줌

        int[] cnt = new int[10];
//        배열 정의 - 자료형, 사이즈 모두 정해줘야함

        for (int i = 0; i < str.length(); i++){
            int num = str.charAt(i) - '0';
//           아스키 값을 기반으로 문자를 숫자로 바꾸는 기법
//            charAt : 주어진 문자열을 아스키값으로 변환
//            '0'의 아스키값은 48
//            str.charAt(i) - '0' = 53 - 48 = 5
//            숫자 5로 변환됨
            cnt[num]++;
        }

        for (int i = 0; i < 10; i++) {
            System.out.println(cnt[i]);
        }
    }
}
