for i=1:300
    str = strcat(num2str(i-1), '.jpg');
    A=imread(str);
    A=imresize(A,0.4);
    [I,map]=rgb2ind(A,256);
    if(i==1)
        imwrite(I,map,'movefig2.gif','DelayTime',0.1,'LoopCount',Inf)
    else
        imwrite(I,map,'movefig2.gif','WriteMode','append','DelayTime',0.1)    
    end
end

