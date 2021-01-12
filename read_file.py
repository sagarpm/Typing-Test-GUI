def file_read():  
  count=0
  para=""
  file=open("paragraph.txt", "r")
  para_dict={}

  for line in file:
    para=line[0:-3]
    count=line[-3:-1]
    para_dict[para]=count
  file.close()
  print(para_dict)

file_read()

#"Mathematicians seek and use patterns to formulate new conjectures they resolve the truth or falsity of such by mathematical proof. When mathematical structures are good models of real phenomena, mathematical reasoning can be used to provide insight or predictions about nature. Through the use of abstraction and logic, mathematics developed from counting, calculation, measurement, and the systematic study of the shapes and motions of physical objects. Practical mathematics has been a human activity from as far back as written records exist."

#The earliest roots of science can be traced to Ancient Egypt and Mesopotamia. Their contributions to mathematics, astronomy, and medicine entered and shaped Greek natural philosophy of classical antiquity, whereby formal attempts were made to provide explanations of events in the physical world based on natural causes.

#Physics is the natural science that studies matter, its motion and behavior through space and time, and the related entities of energy and force.Physics is one of the most fundamental scientific disciplines, and its main goal is to understand how the universe behaves.

#Chemistry is the scientific discipline involved with elements and compounds composed of atoms, molecules and ions their composition, structure, properties, behavior and the changes they undergo during a reaction with other substances. In the scope of its subject, chemistry occupies an intermediate position between physics and biology. It is sometimes called the central science because it provides a foundation for understanding both basic and applied scientific disciplines at a fundamental level.

#Biology is the natural science that studies life and living organisms, including their physical structure, chemical processes, molecular interactions, physiological mechanisms, development and evolution. Despite the complexity of the science, certain unifying concepts consolidate it into a single, coherent field. Biology recognizes the cell as the basic unit of life, genes as the basic unit of heredity, and evolution as the engine that propels the creation and extinction of species.