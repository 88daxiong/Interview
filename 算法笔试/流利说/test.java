/*
 * @Descripttion: 
 * @Author: daxiong
 * @Date: 2019-09-11 21:45:22
 * @LastEditors: daxiong
 * @LastEditTime: 2019-09-11 21:45:22
 */
import java.util.Scanner;

public class test2 {
	//邻接矩阵
	static int[][] graph = new int[200][200];
	//结点个数和边的个数
	static int vNum,eNum;
	//标记矩阵,0为当前结点未访问,1为访问过,-1表示当前结点后边的结点都被访问过。
	static int[] color = new int[200];
	//是否是DAG（有向无环图）
	static boolean isDAG = true;
	
	//图的深度遍历函数
	void DFS(int i){
		System.out.println("正在访问结点"+i);
		//结点i变为访问过的状态
		color[i] = 1;
		for(int j=1;j<=vNum;j++){
			//如果当前结点有指向的结点
			if(graph[i][j] != 0){	
				//并且已经被访问过
				if(color[j] == 1){
					isDAG = false;//有环
					break;
				}else if(color[j] == -1){
					//当前结点后边的结点都被访问过，直接跳至下一个结点
					continue;
				}else{
					DFS(j);//否则递归访问
				}
			}
		}
		//遍历过所有相连的结点后，把本节点标记为-1
		color[i] = -1;
	}
	
	//创建图,以邻接矩阵表示
	void create(){
		Scanner sc = new Scanner(System.in);
		System.out.println("正在创建图，请输入顶点个数vNum：");
		vNum = sc.nextInt();
		System.out.println("请输入边个数eNum：");
		eNum = sc.nextInt();
		//初始化邻接矩阵为0（如果3个顶点，顶点分别是1，2，3）
		for(int i=1;i<=vNum;i++){
			for(int j=1;j<=vNum;j++){
				graph[i][j] = 0;
			}
		}
		for(int k=1;k<=eNum;k++){
			int i = sc.nextInt();
			int j = sc.nextInt();
			graph[i][j] = 1;
		}
		for(int i=1;i<=vNum;i++){
			color[i] = 0;
		}
	}
	
	public static void main(String[] args) {
		test2 t = new test2();
		t.create();
		for(int i=1;i<=vNum;i++){
			if(color[i] == -1){
				continue;
			}
			t.DFS(i);
			if(!isDAG){
				System.out.println("1");
				break;
			}
		}
		if(isDAG){
			System.out.println("0");
		}
	}
}