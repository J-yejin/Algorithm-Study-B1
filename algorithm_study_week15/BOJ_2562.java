// java에서 입력 받기 : Scanner or BufferedReader
// Scanner는 이해는 쉽지만 느림
// BufferedReader는 실전에서 사용, 빠름

import java.io.BufferedReader;
import java.io.InputStreamReader;


public class BOJ_2562 {
    public static void main(String[] args) throws Exception {
//        throws Exception : 에러 나면 그냥 넘기다는 뜻

//        Input 받기
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int max = 0;
        int index = 0;
//        반복문
        for (int i = 1; i<=9; i++){
            int num = Integer.parseInt(br.readLine());
//            한 줄을 문자열로 읽어서 정수(int)로 바꾼다
//            readLine()이 한줄을 문자열로 읽어옴 -> Inter.parseInt 로 정수로 형변환 해주는거
//            그걸 int인 num에 저장

            if (num > max) {
                max = num;
                index = i;
            }
        }
//        자바 출력 함수는 System.out.println (I 아님 l임)
        System.out.println(max);
        System.out.println(index);
    }
}
