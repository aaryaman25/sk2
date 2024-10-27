
skill = input("Enter the skill you want to learn: ")
experience_level = input("Enter your experience level (beginner, intermediate, advanced): ")

skill = skill.lower()  # Convert skill to lowercase for case-insensitive matching

knowledge_base = {
    "python": {
        "beginner": {
            "phases": ["Basic Syntax", "Data Structures", "Control Flow"],
            "resources": {
                "Basic Syntax": ["https://www.w3schools.com/python/python_syntax.asp", "https://docs.python.org/3/tutorial/introduction.html"],
                "Data Structures": ["https://www.w3schools.com/python/python_lists.asp", "https://docs.python.org/3/tutorial/datastructures.html"],
                "Control Flow": ["https://www.w3schools.com/python/python_conditions.asp", "https://docs.python.org/3/tutorial/controlflow.html"]
            },
            "estimated_time": "4 weeks" 
        },
        "intermediate": {
            "phases": ["Object-Oriented Programming", "File Handling", "Modules and Packages"],
            "resources": {
                "Object-Oriented Programming": ["https://realpython.com/python3-object-oriented-programming/", "https://www.programiz.com/python-programming/object-oriented-programming"],
                "File Handling": ["https://www.w3schools.com/python/python_file_handling.asp", "https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files"],
                "Modules and Packages": ["https://realpython.com/python-modules-packages/", "https://docs.python.org/3/tutorial/modules.html"]
            },
            "estimated_time": "6 weeks"
        },
        "advanced": {
            "phases": ["Web Frameworks (e.g., Django/Flask)", "Databases (e.g., SQL/NoSQL)", "Data Science Libraries (e.g., NumPy/Pandas)"],
            "resources": {
                "Web Frameworks (e.g., Django/Flask)": ["https://www.djangoproject.com/", "https://flask.pallets.org/"],
                "Databases (e.g., SQL/NoSQL)": ["https://www.w3schools.com/sql/", "https://www.mongodb.com/"],
                "Data Science Libraries (e.g., NumPy/Pandas)": ["https://numpy.org/", "https://pandas.pydata.org/"]
            },
            "estimated_time": "8+ weeks"
        }
    },
    "web development": {
        "beginner": {
            "phases": ["HTML/CSS", "JavaScript Basics", "Basic Web Design"],
            "resources": {
                "HTML/CSS": ["https://www.w3schools.com/html/", "https://www.w3schools.com/css/"],
                "JavaScript Basics": ["https://www.w3schools.com/js/", "https://developer.mozilla.org/en-US/docs/Web/JavaScript"],
                "Basic Web Design": ["https://www.interaction-design.org/literature/article/principles-of-visual-design", "https://www.invisionapp.com/inside-design/design-principles/"]
            },
            "estimated_time": "6 weeks"
        },
        "intermediate": {
            "phases": ["Responsive Design", "Front-End Frameworks (e.g., React/Angular/Vue)", "Server-Side Basics (e.g., Node.js/Python)"],
            "resources": {
                "Responsive Design": ["https://www.w3schools.com/css/css_rwd_intro.asp", "https://developer.mozilla.org/en-US/docs/Web/CSS/Media_Queries/Using_media_queries"],
                "Front-End Frameworks (e.g., React/Angular/Vue)": ["https://reactjs.org/", "https://angular.io/", "https://vuejs.org/"],
                "Server-Side Basics (e.g., Node.js/Python)": ["https://nodejs.org/en/", "https://www.python.org/"]
            },
            "estimated_time": "8 weeks"
        },
        "advanced": {
            "phases": ["Advanced Frameworks", "Databases (e.g., SQL/NoSQL)", "Web Security", "DevOps"],
            "resources": {
                "Advanced Frameworks": ["https://nextjs.org/", "https://nuxtjs.org/"],
                "Databases (e.g., SQL/NoSQL)": ["https://www.postgresql.org/", "https://www.mongodb.com/"],
                "Web Security": ["https://owasp.org/", "https://portswigger.net/web-security"],
                "DevOps": ["https://www.atlassian.com/devops", "https://aws.amazon.com/devops/"]
            },
            "estimated_time": "12+ weeks"
        }
    },
    "data science": {
        "beginner": {
            "phases": ["Python Fundamentals", "Mathematics for Data Science", "Data Wrangling with Pandas"],
            "resources": {
                "Python Fundamentals": ["https://www.python.org/about/gettingstarted/", "https://www.w3schools.com/python/"],
                "Mathematics for Data Science": ["https://www.khanacademy.org/math/linear-algebra", "https://www.khanacademy.org/math/statistics-probability"],
                "Data Wrangling with Pandas": ["https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html", "https://www.datacamp.com/courses/data-manipulation-with-pandas"]
            },
            "estimated_time": "8 weeks"
        },
        "intermediate": {
            "phases": ["Data Visualization", "Machine Learning Basics", "Statistical Modeling"],
            "resources": {
                "Data Visualization": ["https://matplotlib.org/stable/tutorials/index.html", "https://seaborn.pydata.org/tutorial.html"],
                "Machine Learning Basics": ["https://scikit-learn.org/stable/tutorial/basic/tutorial.html", "https://www.coursera.org/specializations/machine-learning"],
                "Statistical Modeling": ["https://www.statsmodels.org/stable/gettingstarted.html", "https://www.coursera.org/specializations/statistics-with-python"]
            },
            "estimated_time": "10 weeks"
        },
        "advanced": {
            "phases": ["Deep Learning", "Big Data Technologies", "Cloud Computing for Data Science"],
            "resources": {
                "Deep Learning": ["https://www.tensorflow.org/tutorials", "https://pytorch.org/tutorials/"],
                "Big Data Technologies": ["https://spark.apache.org/docs/latest/getting-started.html", "https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-common/SingleCluster.html"],
                "Cloud Computing for Data Science": ["https://aws.amazon.com/machine-learning/", "https://cloud.google.com/ai-platform/"]
            },
            "estimated_time": "12+ weeks"
        }
    },
    "autocad": {
        "beginner": {
            "phases": ["Interface and Basic Tools", "2D Drafting and Drawing", "Basic 3D Modeling"],
            "resources": {
                "Interface and Basic Tools": ["https://www.autodesk.com/products/autocad/free-trial", "https://knowledge.autodesk.com/support/autocad/learn-explore/caas/CloudHelp/cloudhelp/2023/ENU/AutoCAD-Core/files/GUID-D99F6999-4969-4924-8E76-F5C295202321-htm.html"],
                "2D Drafting and Drawing": ["https://www.lynda.com/AutoCAD-tutorials/AutoCAD-2020-Essential-Training/788018-2.html", "https://www.udemy.com/course/autocad-2d-3d-full-course/"],
                "Basic 3D Modeling": ["https://www.autodesk.com/products/autocad/blog/beginner-3d-modeling-autocad/", "https://www.udemy.com/course/autocad-3d-modeling-for-beginners/"]
            },
            "estimated_time": "6 weeks"
        },
        "intermediate": {
            "phases": ["Advanced 3D Modeling", "Working with Layouts and Annotations", "Customization and Automation"],
            "resources": {
                "Advanced 3D Modeling": ["https://www.lynda.com/AutoCAD-tutorials/AutoCAD-Advanced-3D-Modeling/511284-2.html", "https://www.udemy.com/course/autocad-3d-modeling-advanced-level/"],
                "Working with Layouts and Annotations": ["https://knowledge.autodesk.com/support/autocad/learn-explore/caas/CloudHelp/cloudhelp/2023/ENU/AutoCAD-Core/files/GUID-A299E217-B529-457A-9B55-41A20000E41F-htm.html", "https://www.autodesk.com/products/autocad/blog/layouts-and-viewports-in-autocad/"],
                "Customization and Automation": ["https://www.lynda.com/AutoCAD-tutorials/AutoCAD-Customization-Automation/814274-2.html", "https://www.udemy.com/course/autocad-lisp-programming-beginners-to-advanced/"]
            },
            "estimated_time": "8 weeks"
        },
        "advanced": {
            "phases": ["Parametric Modeling and Design", "Advanced Rendering and Visualization", "Collaboration and Data Management"],
            "resources": {
                "Parametric Modeling and Design": ["https://knowledge.autodesk.com/support/autocad/learn-explore/caas/CloudHelp/cloudhelp/2023/ENU/AutoCAD-Core/files/GUID-8809CA6A-E449-489B-927A-B54BF4EE0B09-htm.html", "https://www.autodesk.com/products/autocad/blog/parametric-drawing-and-modeling-in-autocad/"],
                "Advanced Rendering and Visualization": ["https://www.lynda.com/AutoCAD-tutorials/AutoCAD-Rendering/2829303-2.html", "https://www.udemy.com/course/vray-next-for-autocad-complete-guide/"],
                "Collaboration and Data Management": ["https://www.autodesk.com/bim-360/", "https://www.autodesk.com/products/autocad/blog/data-management-and-collaboration-autocad/"]
            },
            "estimated_time": "10+ weeks"
        }
    },
    "cyber security": {
        "beginner": {
            "phases": ["Networking Fundamentals", "Security Concepts", "Linux Basics"],
            "resources": {
                "Networking Fundamentals": ["https://www.comptia.org/certifications/network", "https://www.cybrary.it/course/comptia-network-plus/"],
                "Security Concepts": ["https://www.sans.org/cyber-security-courses/security-essentials/", "https://www.cybrary.it/course/security/"],
                "Linux Basics": ["https://www.linuxfoundation.org/certification/linux-foundation-certified-it-associate-lfc-ita/", "https://www.udemy.com/course/linux-administration-for-beginners/"]
            },
            "estimated_time": "6 weeks"
        },
        "intermediate": {
            "phases": ["Ethical Hacking and Penetration Testing", "Security Operations and Incident Response", "Cryptography"],
            "resources": {
                "Ethical Hacking and Penetration Testing": ["https://www.offensive-security.com/metasploit-training/", "https://www.cybrary.it/course/penetration-testing-with-kali/"],
                "Security Operations and Incident Response": ["https://www.sans.org/cyber-security-courses/security-operations-center-soc-in-depth/", "https://www.cybrary.it/course/soc-analyst/"],
                "Cryptography": ["https://www.coursera.org/specializations/cryptography", "https://www.khanacademy.org/computing/computer-science/cryptography"]
            },
            "estimated_time": "8 weeks"
        },
        "advanced": {
            "phases": ["Malware Analysis", "Security Architecture and Design", "Cloud Security"],
            "resources": {
                "Malware Analysis": ["https://www.sans.org/cyber-security-courses/malware-analysis/", "https://www.cybrary.it/course/malware-analysis/"],
                "Security Architecture and Design": ["https://www.sans.org/cyber-security-courses/security-architecture/", "https://www.cybrary.it/course/security-architecture/"],
                "Cloud Security": ["https://aws.amazon.com/security/", "https://cloud.google.com/security/"]
            },
            "estimated_time": "10+ weeks"
        }
    },
    "game development": {
        "beginner": {
            "phases": ["Game Design Fundamentals", "Programming Basics (Python or C#)", "Game Engine Basics (Unity or Unreal Engine)"],
            "resources": {
                "Game Design Fundamentals": ["https://www.coursera.org/specializations/game-design", "https://www.udemy.com/course/game-design-deep-dive/"],
                "Programming Basics (Python or C#)": ["https://www.w3schools.com/python/", "https://docs.microsoft.com/en-us/dotnet/csharp/"],
                "Game Engine Basics (Unity or Unreal Engine)": ["https://unity.com/learn", "https://www.unrealengine.com/en-US/learn"]
            },
            "estimated_time": "8 weeks"
        },
        "intermediate": {
            "phases": ["Level Design", "Scripting and Gameplay Programming", "2D/3D Art and Animation Basics"],
            "resources": {
                "Level Design": ["https://www.worldofleveldesign.com/", "https://www.udemy.com/course/level-design-master-class/"],
                "Scripting and Gameplay Programming": ["https://docs.unity3d.com/Manual/ScriptingSection.html", "https://docs.unrealengine.com/en-US/Programming/index.html"],
                "2D/3D Art and Animation Basics": ["https://www.blender.org/support/tutorials/", "https://www.udemy.com/course/blender-28-beginner-tutorial/"]
            },
            "estimated_time": "10 weeks"
        },
        "advanced": {
            "phases": ["Advanced Game Mechanics", "Multiplayer Game Development", "Performance Optimization"],
            "resources": {
                "Advanced Game Mechanics": ["https://gameprogrammingpatterns.com/", "https://www.udemy.com/course/advanced-game-development-with-unity/"],
                "Multiplayer Game Development": ["https://docs.unity3d.com/Manual/UNet.html", "https://docs.unrealengine.com/en-US/Gameplay/Networking/index.html"],
                "Performance Optimization": ["https://docs.unity3d.com/Manual/OptimizingGraphicsPerformance.html", "https://docs.unrealengine.com/en-US/Engine/Performance/index.html"]
            },
            "estimated_time": "12+ weeks"
        }
    },
    "ui/ux design": {
        "beginner": {
            "phases": ["Design Thinking", "User Research", "Wireframing and Prototyping"],
            "resources": {
                "Design Thinking": ["https://www.interaction-design.org/literature/article/5-stages-in-the-design-thinking-process", "https://www.ideo.com/human-centered-design-toolkit"],
                "User Research": ["https://www.nngroup.com/articles/user-research-methods/", "https://www.usabilitytesting.com/"],
                "Wireframing and Prototyping": ["https://www.balsamiq.com/", "https://www.figma.com/"]
            },
            "estimated_time": "6 weeks"
        },
        "intermediate": {
            "phases": ["Visual Design and UI Principles", "Usability Testing", "Interaction Design"],
            "resources": {
                "Visual Design and UI Principles": ["https://www.nngroup.com/articles/ten-usability-heuristics/", "https://material.io/design", "https://www.youtube.com/watch?v=QxDkXJeQh9w", "https://www.udemy.com/course/ui-ux-web-design-using-adobe-xd-2020/"],
                "Usability Testing": ["https://www.userzoom.com/", "https://www.trymyui.com/", "https://www.youtube.com/watch?v=qCK7n07_vyo"],
                "Interaction Design": ["https://www.interaction-design.org/literature/article/interaction-design-basics", "https://www.uxcollective.com/", "https://www.youtube.com/watch?v=KV5QlSgq7lg", "https://www.coursera.org/specializations/interaction-design"]
            },
            "estimated_time": "8 weeks"
        },
        "advanced": {
            "phases": ["UX Strategy and Information Architecture", "Design Systems", "Accessibility"],
            "resources": {
                "UX Strategy and Information Architecture": ["https://www.nngroup.com/articles/information-architecture/", "https://www.uxmatters.com/mt/archives/2008/08/information-architecture-for-the-web-and-beyond.php", "https://www.youtube.com/watch?v=bW_nLHFhYM4"],
                "Design Systems": ["https://atlassian.design/", "https://material.io/design/components/", "https://www.youtube.com/watch?v=a5KYlHNKQB0", "https://www.udemy.com/course/design-systems-for-figma/"],
                "Accessibility": ["https://www.w3.org/WAI/fundamentals/", "https://webaim.org/", "https://www.youtube.com/watch?v=20SHvU2Px1g", "https://www.udemy.com/course/web-accessibility-essentials/"]
            },
            "estimated_time": "10+ weeks"
        }
    },
    "mobile app development": {  # New skill: Mobile App Development
        "beginner": {
            "phases": ["Programming Fundamentals (Java/Kotlin/Swift)", "Mobile Platforms (Android/iOS)", "UI Design Basics"],
            "resources": {
                "Programming Fundamentals (Java/Kotlin/Swift)": ["https://www.java.com/en/", "https://kotlinlang.org/", "https://developer.apple.com/swift/"],
                "Mobile Platforms (Android/iOS)": ["https://developer.android.com/", "https://developer.apple.com/ios/"],
                "UI Design Basics": ["https://material.io/design", "https://developer.apple.com/design/human-interface-guidelines/"]
            },
            "estimated_time": "8 weeks"
        },
        "intermediate": {
            "phases": ["Building User Interfaces", "Working with APIs and Data", "App Testing and Debugging"],
            "resources": {
                "Building User Interfaces": ["https://developer.android.com/guide/topics/ui", "https://developer.apple.com/documentation/swiftui/"],
                "Working with APIs and Data": ["https://developer.android.com/training/basics/network-ops/", "https://developer.apple.com/documentation/foundation/url_loading_system/"],
                "App Testing and Debugging": ["https://developer.android.com/studio/debug", "https://developer.apple.com/documentation/xcode/debugging/"]
            },
            "estimated_time": "10 weeks"
        },
        "advanced": {
            "phases": ["Advanced App Architecture", "Performance Optimization", "Publishing and Distribution"],
            "resources": {
                "Advanced App Architecture": ["https://developer.android.com/topic/libraries/architecture", "https://developer.apple.com/documentation/combine"],
                "Performance Optimization": ["https://developer.android.com/topic/performance", "https://developer.apple.com/documentation/xcode/improving_your_app_s_performance"],
                "Publishing and Distribution": ["https://developer.android.com/distribute/marketing-tools/linking-to-google-play", "https://developer.apple.com/app-store/submissions/"]
            },
            "estimated_time": "12+ weeks"
        }
    },
    "cloud computing": {  # New skill: Cloud Computing
        "beginner": {
            "phases": ["Cloud Concepts", "Virtualization", "Cloud Providers (AWS/Azure/GCP)"],
            "resources": {
                "Cloud Concepts": ["https://www.youtube.com/watch?v=dH0yz-PxSec", "https://www.coursera.org/specializations/cloud-computing"],
                "Virtualization": ["https://www.vmware.com/topics/glossary/content/virtualization", "https://www.youtube.com/watch?v=oG-51oWCF7w"],
                "Cloud Providers (AWS/Azure/GCP)": ["https://aws.amazon.com/", "https://azure.microsoft.com/en-us/", "https://cloud.google.com/"]
            },
            "estimated_time": "6 weeks"
        },
        "intermediate": {
            "phases": ["Networking and Security", "Storage and Databases", "Compute Services"],
            "resources": {
                "Networking and Security": ["https://aws.amazon.com/vpc/", "https://azure.microsoft.com/en-us/services/virtual-network/", "https://cloud.google.com/vpc/"],
                "Storage and Databases": ["https://aws.amazon.com/s3/", "https://azure.microsoft.com/en-us/services/storage/", "https://cloud.google.com/storage/"],
                "Compute Services": ["https://aws.amazon.com/ec2/", "https://azure.microsoft.com/en-us/services/virtual-machines/", "https://cloud.google.com/compute/"]
            },
            "estimated_time": "8 weeks"
        },
        "advanced": {
            "phases": ["Serverless Computing", "Containers and Orchestration", "Cloud Automation"],
            "resources": {
                "Serverless Computing": ["https://aws.amazon.com/lambda/", "https://azure.microsoft.com/en-us/services/functions/", "https://cloud.google.com/functions/"],
                "Containers and Orchestration": ["https://aws.amazon.com/ecs/", "https://azure.microsoft.com/en-us/services/kubernetes-service/", "https://cloud.google.com/kubernetes-engine/"],
                "Cloud Automation": ["https://aws.amazon.com/cloudformation/", "https://azure.microsoft.com/en-us/services/azure-resource-manager/", "https://cloud.google.com/deployment-manager/"]
            },
            "estimated_time": "12+ weeks"
        }
    },
    "java programming": {
        "beginner": {
            "phases": ["Basic Syntax and Data Types", "Object-Oriented Programming Concepts", "Control Flow and Loops"],
            "resources": {
                "Basic Syntax and Data Types": ["https://www.w3schools.com/java/", "https://docs.oracle.com/javase/tutorial/java/nutsandbolts/"],
                "Object-Oriented Programming Concepts": ["https://www.tutorialspoint.com/java/java_object_oriented_programming.htm", "https://www.geeksforgeeks.org/object-oriented-programming-concepts-in-java/"],
                "Control Flow and Loops": ["https://www.w3schools.com/java/java_control_statements.asp", "https://docs.oracle.com/javase/tutorial/java/nutsandbolts/flow.html"]
            },
            "estimated_time": "6 weeks"
        },
        "intermediate": {
            "phases": ["Collections and Generics", "Exception Handling", "File I/O"],
            "resources": {
                "Collections and Generics": ["https://www.geeksforgeeks.org/collections-in-java/", "https://docs.oracle.com/javase/tutorial/collections/"],
                "Exception Handling": ["https://www.w3schools.com/java/java_exceptions.asp", "https://docs.oracle.com/javase/tutorial/essential/exceptions/"],
                "File I/O": ["https://www.tutorialspoint.com/java/java_files_io.htm", "https://docs.oracle.com/javase/tutorial/essential/io/"]
            },
            "estimated_time": "8 weeks"
        },
        "advanced": {
            "phases": ["Multithreading and Concurrency", "Networking", "Java EE or Spring Framework"],
            "resources": {
                "Multithreading and Concurrency": ["https://www.geeksforgeeks.org/multithreading-in-java/", "https://docs.oracle.com/javase/tutorial/essential/concurrency/"],
                "Networking": ["https://www.javatpoint.com/java-networking", "https://docs.oracle.com/javase/tutorial/networking/"],
                "Java EE or Spring Framework": ["https://www.oracle.com/java/technologies/java-ee-glance.html", "https://spring.io/"]
            },
            "estimated_time": "12+ weeks"
        }
    },
    "javascript programming": {
        "beginner": {
            "phases": ["Variables, Data Types, and Operators", "Control Flow and Loops", "Functions"],
            "resources": {
                "Variables, Data Types, and Operators": ["https://www.w3schools.com/js/js_variables.asp", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types"],
                "Control Flow and Loops": ["https://www.w3schools.com/js/js_if_else.asp", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling"],
                "Functions": ["https://www.w3schools.com/js/js_function_definition.asp", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions"]
            },
            "estimated_time": "4 weeks"
        },
        "intermediate": {
            "phases": ["Objects and Prototypes", "DOM Manipulation", "Asynchronous Programming"],
            "resources": {
                "Objects and Prototypes": ["https://www.w3schools.com/js/js_objects.asp", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Working_with_Objects"],
                "DOM Manipulation": ["https://www.w3schools.com/js/js_htmldom.asp", "https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/"],
                "Asynchronous Programming": ["https://www.w3schools.com/js/js_ajax_intro.asp", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Events"]
            },
            "estimated_time": "6 weeks"
        },
        "advanced": {
            "phases": ["Node.js and Express.js", "React or Angular or Vue.js", "Testing and Debugging"],
            "resources": {
                "Node.js and Express.js": ["https://nodejs.org/en/", "https://expressjs.com/"],
                "React or Angular or Vue.js": ["https://reactjs.org/", "https://angular.io/", "https://vuejs.org/"],
                "Testing and Debugging": ["https://jestjs.io/", "https://jasmine.github.io/", "https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/debugger"]
            },
            "estimated_time": "8+ weeks"
        }
    },
    "c++ programming": {
        "beginner": {
            "phases": ["Basic Syntax and Data Types", "Control Flow and Loops", "Functions"],
            "resources": {
                "Basic Syntax and Data Types": ["https://www.w3schools.com/cpp/", "https://en.cppreference.com/w/cpp/language/basic_concepts"],
                "Control Flow and Loops": ["https://www.w3schools.com/cpp/cpp_control_statements.asp", "https://en.cppreference.com/w/cpp/language/statements"],
                "Functions": ["https://www.w3schools.com/cpp/cpp_functions.asp", "https://en.cppreference.com/w/cpp/language/functions"]
            },
            "estimated_time": "6 weeks"
        },
        "intermediate": {
            "phases": ["Object-Oriented Programming", "Pointers and Memory Management", "Standard Template Library (STL)"],
            "resources": {
                "Object-Oriented Programming": ["https://www.tutorialspoint.com/cplusplus/cpp_object_oriented_programming.htm", "https://en.cppreference.com/w/cpp/language/classes"],
                "Pointers and Memory Management": ["https://www.geeksforgeeks.org/pointers-in-c-and-cpp/", "https://en.cppreference.com/w/cpp/language/memory_model"],
                "Standard Template Library (STL)": ["https://www.cplusplus.com/reference/stl/", "https://en.cppreference.com/w/cpp/header"]
            },
            "estimated_time": "8 weeks"
        },
        "advanced": {
            "phases": ["Templates and Metaprogramming", "Exception Handling", "Concurrency and Multithreading"],
            "resources": {
                "Templates and Metaprogramming": ["https://www.geeksforgeeks.org/templates-cpp/", "https://en.cppreference.com/w/cpp/language/templates"],
                "Exception Handling": ["https://www.tutorialspoint.com/cplusplus/cpp_exceptions_handling.htm", "https://en.cppreference.com/w/cpp/language/exceptions"],
                "Concurrency and Multithreading": ["https://www.cplusplus.com/reference/thread/", "https://en.cppreference.com/w/cpp/thread"]
            },
            "estimated_time": "12+ weeks"
        }
    },
    "c# programming": {
        "beginner": {
            "phases": ["Basic Syntax and Data Types", "Object-Oriented Programming Concepts", "Control Flow and Loops"],
            "resources": {
                "Basic Syntax and Data Types": ["https://www.w3schools.com/cs/", "https://docs.microsoft.com/en-us/dotnet/csharp/tour-of-csharp/"],
                "Object-Oriented Programming Concepts": ["https://www.tutorialspoint.com/csharp/csharp_object_oriented_programming.htm", "https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/object-oriented-programming"],
                "Control Flow and Loops": ["https://www.w3schools.com/cs/cs_control_statements.asp", "https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/statements-expressions-operators/statements"]
            },
            "estimated_time": "6 weeks"
        },
        "intermediate": {
            "phases": ["LINQ and Lambda Expressions", "Generics and Collections", "File I/O and Serialization"],
            "resources": {
                "LINQ and Lambda Expressions": ["https://www.tutorialsteacher.com/linq/linq-tutorials", "https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/linq/"],
                "Generics and Collections": ["https://www.tutorialspoint.com/csharp/csharp_generics.htm", "https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/generics/"],
                "File I/O and Serialization": ["https://www.dotnetperls.com/file", "https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/serialization/"]
            },
            "estimated_time": "8 weeks"
        },
        "advanced": {
            "phases": ["ASP.NET Core MVC", "Entity Framework Core", "Asynchronous Programming and Multithreading"],
            "resources": {
                "ASP.NET Core MVC": ["https://www.tutorialsteacher.com/mvc/asp.net-mvc-tutorials", "https://docs.microsoft.com/en-us/aspnet/core/mvc/overview?view=aspnetcore-6.0"],
                "Entity Framework Core": ["https://www.entityframeworktutorial.net/", "https://docs.microsoft.com/en-us/ef/core/"],
                "Asynchronous Programming and Multithreading": ["https://www.dotnetperls.com/async", "https://docs.microsoft.com/en-us/dotnet/csharp/programming-guide/concepts/async/"]
            },
            "estimated_time": "12+ weeks"
        }
    },
    "go programming": {
        "beginner": {
            "phases": ["Basic Syntax and Data Types", "Control Flow and Loops", "Functions"],
            "resources": {
                "Basic Syntax and Data Types": ["https://go.dev/tour/", "https://www.tutorialspoint.com/go/go_basic_syntax.htm"],
                "Control Flow and Loops": ["https://www.tutorialspoint.com/go/go_decision_making.htm", "https://go.dev/tour/flowcontrol/1"],
                "Functions": ["https://www.tutorialspoint.com/go/go_functions.htm", "https://go.dev/tour/basics/4"]
            },
            "estimated_time": "4 weeks"
        },
        "intermediate": {
            "phases": ["Data Structures and Algorithms", "Concurrency and Goroutines", "Networking"],
            "resources": {
                "Data Structures and Algorithms": ["https://www.geeksforgeeks.org/data-structures-in-golang/", "https://golang.org/pkg/container/"],
                "Concurrency and Goroutines": ["https://www.golangprograms.com/goroutines.html", "https://go.dev/tour/concurrency/1"],
                "Networking": ["https://www.geeksforgeeks.org/socket-programming-golang/", "https://golang.org/pkg/net/"]
            },
            "estimated_time": "6 weeks"
        },
        "advanced": {
            "phases": ["Web Development with Gin or Echo", "Microservices and gRPC", "Testing and Debugging"],
            "resources": {
                "Web Development with Gin or Echo": ["https://gin-gonic.com/", "https://echo.labstack.com/"],
                "Microservices and gRPC": ["https://grpc.io/", "https://developers.google.com/protocol-buffers/"],
                "Testing and Debugging": ["https://golang.org/pkg/testing/", "https://github.com/go-delve/delve"]
            },
            "estimated_time": "8+ weeks"
        }
    },
    "swift programming": {
        "beginner": {
            "phases": ["Basic Syntax and Data Types", "Control Flow and Loops", "Functions"],
            "resources": {
                "Basic Syntax and Data Types": ["https://docs.swift.org/swift-book/LanguageGuide/TheBasics.html", "https://www.tutorialspoint.com/swift/swift_basic_syntax.htm"],
                "Control Flow and Loops": ["https://docs.swift.org/swift-book/LanguageGuide/ControlFlow.html", "https://www.tutorialspoint.com/swift/swift_control_flow.htm"],
                "Functions": ["https://docs.swift.org/swift-book/LanguageGuide/Functions.html", "https://www.tutorialspoint.com/swift/swift_functions.htm"]
            },
            "estimated_time": "4 weeks"
        },
        "intermediate": {
            "phases": ["Object-Oriented Programming", "Optionals and Error Handling", "Closures"],
            "resources": {
                "Object-Oriented Programming": ["https://docs.swift.org/swift-book/LanguageGuide/Initialization.html", "https://www.tutorialspoint.com/swift/swift_classes_objects.htm"],
                "Optionals and Error Handling": ["https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html", "https://www.tutorialspoint.com/swift/swift_optionals.htm"],
                "Closures": ["https://docs.swift.org/swift-book/LanguageGuide/Closures.html", "https://www.tutorialspoint.com/swift/swift_closures.htm"]
            },
            "estimated_time": "6 weeks"
        },
        "advanced": {
            "phases": ["iOS App Development with SwiftUI", "Networking and APIs", "Concurrency with Grand Central Dispatch"],
            "resources": {
                "iOS App Development with SwiftUI": ["https://developer.apple.com/tutorials/swiftui/", "https://www.hackingwithswift.com/quick-start/swiftui/"],
                "Networking and APIs": ["https://developer.apple.com/documentation/foundation/urlsession", "https://www.raywenderlich.com/7914-alamofire-tutorial-getting-started"],
                "Concurrency with Grand Central Dispatch": ["https://developer.apple.com/documentation/dispatch", "https://www.raywenderlich.com/5376-grand-central-dispatch-tutorial-for-swift-4-part-1-2"]
            },
            "estimated_time": "8+ weeks"
        }
    },
    "kotlin programming": {
        "beginner": {
            "phases": ["Basic Syntax and Data Types", "Control Flow and Loops", "Functions"],
            "resources": {
                "Basic Syntax and Data Types": ["https://kotlinlang.org/docs/basic-syntax.html", "https://www.tutorialspoint.com/kotlin/kotlin_basic_syntax.htm"],
                "Control Flow and Loops": ["https://kotlinlang.org/docs/control-flow.html", "https://www.tutorialspoint.com/kotlin/kotlin_control_flow.htm"],
                "Functions": ["https://kotlinlang.org/docs/functions.html", "https://www.tutorialspoint.com/kotlin/kotlin_functions.htm"]
            },
            "estimated_time": "4 weeks"
        },
        "intermediate": {
            "phases": ["Object-Oriented Programming", "Null Safety", "Collections"],
            "resources": {
                "Object-Oriented Programming": ["https://kotlinlang.org/docs/classes.html", "https://www.tutorialspoint.com/kotlin/kotlin_classes_objects.htm"],
                "Null Safety": ["https://kotlinlang.org/docs/null-safety.html", "https://www.baeldung.com/kotlin-null-safety"],
                "Collections": ["https://kotlinlang.org/docs/collections-overview.html", "https://www.tutorialspoint.com/kotlin/kotlin_collections.htm"]
            },
            "estimated_time": "6 weeks"
        },
        "advanced": {
            "phases": ["Android App Development", "Coroutines", "Testing and Debugging"],
            "resources": {
                "Android App Development": ["https://developer.android.com/kotlin", "https://www.raywenderlich.com/kotlin"],
                "Coroutines": ["https://kotlinlang.org/docs/coroutines-overview.html", "https://www.baeldung.com/kotlin-coroutines"],
                "Testing and Debugging": ["https://kotlinlang.org/docs/testing.html", "https://developer.android.com/studio/debug"]
            },
            "estimated_time": "8+ weeks"
        }
    },
    "r programming": {
        "beginner": {
            "phases": ["Basic Syntax and Data Types", "Data Structures", "Control Flow"],
            "resources": {
                "Basic Syntax and Data Types": ["https://www.r-project.org/", "https://www.tutorialspoint.com/r/r_basic_syntax.htm"],
                "Data Structures": ["https://www.tutorialspoint.com/r/r_data_types.htm", "https://www.statmethods.net/input/datatypes.html"],
                "Control Flow": ["https://www.tutorialspoint.com/r/r_control_statements.htm", "https://www.statmethods.net/basics/flowcontrol.html"]
            },
            "estimated_time": "4 weeks"
        },
        "intermediate": {
            "phases": ["Data Manipulation with dplyr", "Data Visualization with ggplot2", "Statistical Modeling"],
            "resources": {
                "Data Manipulation with dplyr": ["https://dplyr.tidyverse.org/", "https://www.datacamp.com/courses/data-manipulation-with-dplyr"],
                "Data Visualization with ggplot2": ["https://ggplot2.tidyverse.org/", "https://www.datacamp.com/courses/data-visualization-with-ggplot2"],
                "Statistical Modeling": ["https://www.statmethods.net/stats/regression.html", "https://www.datacamp.com/courses/statistical-modeling-in-r"]
            },
            "estimated_time": "6 weeks"
        },
        "advanced": {
            "phases": ["Machine Learning with caret", "Shiny Web Applications", "Advanced Statistical Techniques"],
            "resources": {
                "Machine Learning with caret": ["https://topepo.github.io/caret/", "https://www.datacamp.com/courses/machine-learning-toolbox-in-r"],
                "Shiny Web Applications": ["https://shiny.rstudio.com/", "https://www.datacamp.com/courses/building-web-applications-with-shiny-in-r"],
                "Advanced Statistical Techniques": ["https://www.statmethods.net/advstats/anova.html", "https://www.datacamp.com/courses/advanced-statistical-modeling-in-r"]
            },
            "estimated_time": "8+ weeks"
        }
    }
}


if skill in knowledge_base:
    if experience_level in knowledge_base[skill]:
        roadmap = knowledge_base[skill][experience_level]
        print("\nRoadmap for", skill, "(", experience_level, "):")
        for phase in roadmap["phases"]:
            print("\nPhase:", phase)
            print("Resources:")
            for resource in roadmap["resources"][phase]:
                print("-", resource)
        print("\nEstimated Time:", roadmap["estimated_time"])
    else:
        print("Roadmap for", experience_level, "level in", skill, "is not available yet.")
else:
    print("Roadmap for", skill, "is not available yet.")


if skill in knowledge_base:
    if experience_level in knowledge_base[skill]:
        roadmap = knowledge_base[skill][experience_level]
        print("\nRoadmap for", skill, "(", experience_level, "):")
        for phase in roadmap["phases"]:
            print("\nPhase:", phase)
            print("Resources:")
            for resource in roadmap["resources"][phase]:
                print("-", resource)
        print("\nEstimated Time:", roadmap["estimated_time"])
    else:
        print("Roadmap for", experience_level, "level in", skill, "is not available yet.")
else:
    print("Roadmap for", skill, "is not available yet.")
