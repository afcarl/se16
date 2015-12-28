# Architectures

[TOC]

todo:

+ add notes from https://www.evernote.com/shard/s14/sh/f4f0b03f-4f57-42fb-8a1e-db9a3235d522/ad332a2c5889878b
+ add notes from my talk at icse

_____

The world is a big place

![](/_img/architecture.png)

Need **architectures** to divide complex parts into manageable bits.

# Classic Examples

Classic pipe and filter. Used in UNIX (bad to
interaction across multiple pipes; good for easy
development, ease of maintenance)

![](/_img/pipe_and_filter.jpg)

Lots of small little programs, each focused on one task, ready to be combined in different ways:

```bash
# find biggest files changed in August
ls -l | grep "Aug" | sort +4n | more

# apply the table (tbl) and picture (pic)
# and equation (eqn) to all the manuscript (.ms) files
	
cat *.ms |
tbl |
pic |
eqn |
troff -t  -ps > out.ps
```

LAMP = Linux apache mysql php (python)

![](/_img/LAMPStack.png)

After LAMP, comes MEAN (requires you to work in Javascript):

![](/_img/mean-stack.png)

MVC: good for tight/complex interaction. Complex to maintain

![](/_img/MVC-2.png)

Subject-observer. multiple views on one model

![](/_img/obser023.gif)

Looser collaboration with publish, subscribe

<img src="/_img/pub-sub.png" width=600>

# Layers

The following notes are
from  the [MSDN](https://msdn.microsoft.com/en-us/library/ee658117.aspx) notes.

## Client/Server (layers=2)

Segregates the system into two applications, where
the client makes requests to the server. In many
cases, the server is a database with application
logic represented as stored procedures.

Advantages

+ Higher security. All data is stored on the server, which generally offers a greater control of security than client machines.
+ Centralized data access. Because data is stored only on the server, access and updates to the data are far easier to administer than in other architectural styles.
+ Ease of maintenance. Roles and responsibilities of a computing system are distributed among several servers that are known to each other through a network. This ensures that a client remains unaware and unaffected by a server repair, upgrade, or relocation.

## N-Tier / 3-Tier (layers=3)

Segregates functionality into separate segments in
much the same way as the layered style, but with
each segment being a tier located on a physically
separate computer.

## Layered Architecture (layers=3)

Partitions the concerns of the application into stacked groups (layers).

Advantages:

+ Abstraction. Layered architecture abstracts the
  view of the system as whole while providing enough
  detail to understand the roles and
  responsibilities of individual layers and the
  relationship between them.
+ Encapsulation. No assumptions need to be made
  about data types, methods and properties, or
  implementation during design, as these features
  are not exposed at layer boundaries.
+ Clearly defined functional layers. The separation
  between functionality in each layer is
  clear. Upper layers such as the presentation layer
  send commands to lower layers, such as the
  business and data layers, and may react to events
  in these layers, allowing data to flow both up and
  down between the layers.
+ High cohesion. Well-defined responsibility
  boundaries for each layer, and ensuring that each
  layer contains functionality directly related to
  the tasks of that layer, will help to maximize
  cohesion within the layer.
+ Reusable. Lower layers have no dependencies on
  higher layers, potentially allowing them to be
  reusable in other scenarios.
+ Loose coupling. Communication between layers is
  based on abstraction and events to provide loose
  coupling between layers.
+ Separation of concerns. Separated Presentation
  patterns divide UI processing concerns into
  distinct roles; for example, MVC has three roles:
  the Model, the View, and the Controller. The Model
  represents data (perhaps a domain model that
  includes business rules); the View represents the
  UI; and the Controller handles requests,
  manipulates the model, and performs other
  operations.
+ Event-based notification. The Observer pattern is
  commonly used to provide notifications to the View
  when data managed by the Model changes.
+ Delegated event handling. The controller handles
  events triggered from the UI controls in the View.

(Reality check: lately there has much movement away from LAMP towards
MEAN since LAMP is harder to modify (quickly) and test.)

# Parts

## Pipe-and-Filter

Notes from [David  March](http://www4.desales.edu/~dlm1/it533/class03/pipe.html):

Advantages:

+ Filters stand alone and can be treated as black
  boxes. This isolation of functionality helps to
  ensure quality attributes such as information
  hiding, high cohesion, modifiability, and reuse.
+ Filters interact with other components in limited
  ways. This connection simplicity helps to ensure
  low coupling.  Pipes and filters can be
  hierarchically composed. Higher order filters can
  be created from any combination of lower order
  pipes and filters.
+ The construction of the pipe and filter sequence
  can often be delayed until runtime (late
  binding). This permits a controller component to
  tailor a process based on the current state of the
  application.
+ Because the process performed by the filter is
  isolated from the other components in the system,
  it is relatively easy to run a pipe-and-filter
  system on parallel processors or in multiple
  threads on a single processor.

Disadvantages (Top) 

+ Because the problem is decomposed into sequential
  steps, a batch mentality is encouraged. It is
  difficult to create entire interactive
  applications using this style.
+ Filters often force the data to be represented in
  the lowest common denominator, typically byte or
  character streams. This means that if processing
  must be based on information tokens (words, lines,
  records), every filter may introduce overhead for
  parsing and unparsing the data stream.
+ If a filter can not produce any output until it
  has received all of its input, the filter will
  require a buffer of unlimited size. If fixed size
  buffers are used, the system could deadlock. A
  sort filter has this problem.

## Component-Based Architecture

Decomposes application design into reusable
functional or logical components that expose
well-defined communication interfaces.

Advantages (best case... not always realized...):

+ Reusable. Components are usually designed to be
  reused in different scenarios in different
  applications. However, some components may be
  designed for a specific task.
     + Ease of development. Components implement
       well-known interfaces to provide defined
       functionality, allowing development without
       impacting other parts of the system.
+ Replaceable. Components may be readily substituted
  with other similar components.
+ Ease of deployment. As new compatible versions
  become available, you can replace existing
  versions with no impact on the other components or
  the system as a whole.
+ Not context specific. Components are designed to
  operate in different environments and
  contexts. Specific information, such as state
  data, should be passed to the component instead of
  being included in or accessed by the component.
+ Extensible. A component can be extended from
  existing components to provide new behavior.
      + Reduced cost. The use of third-party
        components allows you to spread the cost of
        development and maintenance.
+ Encapsulated. Components expose interfaces that
  allow the caller to use its functionality, and do
  not reveal details of the internal processes or
  any internal variables or state.
+ Independent. Components are designed to have
  minimal dependencies on other
  components. Therefore components can be deployed
  into any appropriate environment without affecting
  other components or systems.

## Object-Oriented

A design paradigm based on division of
responsibilities for an application or system into
individual reusable and self-sufficient objects,
each containing the data and the behavior relevant
to the object.

Advantages:

+ See _Components_


# Other

## Domain Driven Design

An object-oriented architectural style focused on
modeling a business domain and defining business
objects based on entities within the business
domain.

Advantages:

+ Communication. All parties within a development
  team can use the domain model and the entities it
  defines to communicate business knowledge and
  requirements using a common business domain
  language, without requiring technical jargon.
+ Extensible. The domain model is often modular and
  flexible, making it easy to update and extend as
  conditions and requirements change.

## Message Bus

An architecture style that prescribes use of a
software system that can receive and send messages
using one or more communication channels, so that
applications can interact without needing to know
specific details about each other.

Advantages:

+ Loose coupling. As long as applications expose a
  suitable interface for communication with the
  message bus, there is no dependency on the
  application itself, allowing changes, updates, and
  replacements that expose the same interface.
        + Message-oriented communications. All communication
          between applications is based on messages that use
          known schemas. 
+ Scalability. Multiple instances of the same
  application can be attached to the bus in order to
  handle multiple requests at the same time.
+ Complex processing logic. Complex operations can
  be executed by combining a set of smaller
  operations, each of which supports specific tasks,
  as part of a multistep itinerary.
+ Modifications to processing logic. Because
  interaction with the bus is based on common
  schemas and commands, you can insert or remove
  applications on the bus to change the logic that
  is used to process messages.
+ Integration with different environments. By using
  a message-based communication model based on
  common standards, you can interact with
  applications developed for different environments,
  such as Microsoft .NET and Java.

## Service-Oriented Architecture (SOA)

Refers to applications that expose and consume
functionality as a service using contracts and
messages.

Advantages:

+ Services are autonomous. Each service is
  maintained, developed, deployed, and versioned
  independently.
+ Services are distributable. Services can be
  located anywhere on a network, locally or
  remotely, as long as the network supports the
  required communication protocols.
+ Services are loosely coupled. Each service is
  independent of others, and can be replaced or
  updated without breaking applications that use it
  as long as the interface is still compatible.
+ Services share schema and contract, not
  class. Services share contracts and schemas when
  they communicate, not internal classes.
+ Compatibility is based on policy. Policy in this
  case means definition of features such as
  transport, protocol, and security.

## Etc, etc

Combinations, variants of the above (maybe with other stuff).



