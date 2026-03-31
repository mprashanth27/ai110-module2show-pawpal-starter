classDiagram
    class Owner {
        +String name
        +String address
        +String contact
        +List~Pet~ pets
        +do_task(task: Task) void
        +add_pet(pet: Pet) void
    }

    class Pet {
        +String name
        +String breed
        +List~Task~ tasks
    }

    class Task {
        +String name
        +String location
        +DateTime time
        +String status
        +String description
        +int priority
        +create() Task
        +edit(field: String, value: String) void
        +delete() void
        +reschedule(new_time: DateTime) void
    }

    class Scheduler {
        +List~Task~ schedule
        +List~Task~ appointments
        +book_appointment(task: Task) void
        +prioritize_tasks() List~Task~
        +get_upcoming(hours: int) List~Task~
        +cancel_appointment(task: Task) void
    }

    Owner "1" --> "1..*" Pet : owns
    Owner "1" --> "0..*" Task : assigned to
    Pet "1" --> "0..*" Task : has
    Scheduler "1" --> "0..*" Task : manages
    Owner "1" --> "1" Scheduler : uses
