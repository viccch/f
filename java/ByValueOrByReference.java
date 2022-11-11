public class ByValueOrByReference {
    int x;

    public static void changeName(Person p1, Person p2) {

        p1.setName("Lisi");
        p2.setName("Zhangsan");
    }

    public static void swap(Person p1, Person p2) {
        Person temp=p1;
        p1=p2;
        p2=temp;//只是引用，退出后失效
    }

    public static void main(String[] args) {
        Person p1=new Person("Zhangsan");
        Person p2=new Person("Lisi");

        changeName(p1,p2);
        System.out.println(p1.getName()+"/"+p2.getName());

        swap(p1, p2);
        System.out.println(p1.getName()+"/"+p2.getName());

    }
}

class Person {
    private String name;

    public Person(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
}