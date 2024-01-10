#from pyodide import Element,write
import asyncio
w=Element('w')
o1=Element('o1')
o2=Element('o2')
l=Element('l')
y=Element('y')
w2=Element('w2')
e=Element('e')
b=Element('b')
async def fw():
    await asyncio.sleep(0.5)
    w.write('W')
    #await asyncio.sleep(0.5)
async def fo1():
    await asyncio.sleep(1)
    o1.write('O')
    
async def fo2():
    await asyncio.sleep(1.5)
    o2.write('O')
    
async def fl():
    await asyncio.sleep(2)
    l.write('L')
    
async def fy():
    await asyncio.sleep(2.5)
    y.write('Y')
    
async def fw2():
    await asyncio.sleep(3)
    w2.write('W')
   
async def fe():
    await asyncio.sleep(3.5)
    e.write('E')
    
async def fb():
    await asyncio.sleep(4)
    b.write('B')
async def end():
    await asyncio.sleep(5)
    Element("co-name").write("WOOLY WEB")
async def main():
    t1=asyncio.create_task(fw());
    t2=asyncio.create_task(fo1());
    t3=asyncio.create_task(fo2());
    t4=asyncio.create_task(fl());
    t5=asyncio.create_task(fy());
    t6=asyncio.create_task(fw2());
    t7=asyncio.create_task(fe());
    t8=asyncio.create_task(fb());
    t9=asyncio.create_task(end());
    await t9
    
    
await main()

