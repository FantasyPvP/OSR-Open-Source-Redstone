class main():

    function @default():
        INT num = $input("enter an integer")
        loop i, if i < num, i += 1:
            $output(@secondary(i))
            $output(STR "hello world")
        &return()

    function @secondary(i):
        INT x = i + i
        INT y = i - x
        &return(y)
