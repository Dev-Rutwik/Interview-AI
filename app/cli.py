from workflows.interview_graph import build_interview_flow

def run_interview(resume_text):
    interview_flow = build_interview_flow()
    interview_flow.invoke({
        "resume_text": resume_text,
        "clusters": {},
        "current_cluster": 0,
        "current_question": "",
        "user_response": "",
        "follow_up_needed": True
    })

if __name__ == "__main__":
        resume  = """Rutwik Kadam Email : rutwik2602@gmail.com   Phone:9284908856        LinkedIn : https://www.linkedin.com/in/rutwik -kadam -1a2b36273/       
GitHub : R2602    Projects : Netlify   
         
PROJECTS  
 Maze Game with Pathfinding Algorithms  
• Developed  a Maze Game in Python using Tkinter and Turtle, integrating DFS, BFS, and A* for competitive gameplay.  
• Designed  core features like maze generation, player interaction, and algorithmic competition for smooth performance.  
• Implemented  a GUI with responsive controls, enhancing user engagement by 40% through an interactive learning experience.  
• Delivered  a polished, well -tested game balancing algorithmic theory, UI design, and robust gameplay mechanics.  
WORK EXPERIENCE  
Internet Soft  – Jan 2025 - present  
Software Developer  
• Developed scalable Python backend services  using FastAPI , enabling fast and efficient API development for automation 
and AI -driven workflows.  
• Built and deployed an Automation  Dashboard  with Streamlit , integrated with real -time test execution and reporting tools, 
reducing manual QA by 50%. 
• Utilized GitHub  for version control , CI/CD workflows , and collaborative development, ensuring smooth and structured 
code management.  
• Leveraged ngrok  for secure local server tunneling , enabling real -time testing and remote access to locally hosted 
applications during development.  
ACHIEVEMENTS  
1. A Secured 3rd prize  by leading a team in the Hack MIT Hackathon , demonstrating exceptional leadership and 
teamwork . 
2. Researched  and presented  on "Quantum Computing and Teleportation,"  exploring advanced quantum mechanics  
concepts and applications.  
CERTIFICATES  
1. Completed Google's Data Analytics Specialization  (November 2021), gaining expertise in data analysis , data cleaning , 
data visualization  with Tableau , and statistical analysis . 
Course Link  | Credentials : QBQFC3A6CMM2  
2. Completed Python for Everybody Specialization  by the University of Michigan  (October 2021), learning Python 
programming , data processing , API handling , and automation . 
Course Link  | Credentials : BRJEHTMYNE44  
 EDUCATION   
MIT WPU , Pune  (Masters of Computer Science ) Aug 2023 - Dec 2024 
Coursework : Data Structures, SQL, NoSQL, Agile / Scrum methodologies, Object -Oriented Programming . CGPA:  8.28/10.0  
Modern College of Science,  Pune  (Bachelor of Computer Science ) July 2020-2023  
Coursework : Mathematics, Theory of computation, Software Development, HTML, CSS, JavaScript , 
Networking . CGPA:9.22/10.0  
SKILLS   
Languages :    Python, JavaScript, Data Structure & Algorithms . 
Technologies :  Git/GitHub, MySQL, MongoDB, Pandas, NumPy, Lang Chain,  Lang Graph, Stream lit, Web Extraction, Machine 
Learning, Deep Learning, Artificial Intelligence, vector Database - Chroma, Llama Index, Selenium, Appium, Automation, GitHub 
Actions , FastAPI . 
Personality :  Leadership, problem -solving, Communication, Teamwork, Growth Oriented, Performance Focused."""
    
        run_interview(resume)
