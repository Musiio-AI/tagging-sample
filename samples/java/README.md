# Java Samples

## Set up Maven project

The Java sample shown here uses [Maven](https://spring.io/guides/gs/maven/) as the Java project management tool. Hence, a `pom.xml` file is required for installing dependencies necessary to run the code samples.

Initialize your Maven project, in this example, we will use the following project configuration:

```xml
<groupId>com.example.tagging</groupId>
<artifactId>tagging</artifactId>
```

Your project structure will look something like this:

```
(/samples/tagging/java/)
- tagging/
  | - src/
  |   | - main/com/example/tagging/
  |   | - test/
  | - target/
  | - pom.xml
```

Open `pom.xml` and add the following dependencies in the `<dependencies></dependencies>` tag

```xml
<!-- https://mvnrepository.com/artifact/org.springframework.boot/spring-boot-starter-web -->
<dependency>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-starter-web</artifactId>
  <version>2.3.3.RELEASE</version>
</dependency>
```

Copy and paste the code samples Java files in `samples/tagging/java/` into your project folder `tagging/src/main/com/example/tagging/` such that your project structure looks something like this:

```
(/samples/tagging/java/)
- tagging/
  | - src/
  |   | - main/com/example/tagging/
  |   |   | - AudioLinkUpload.java
  |   |   |	- AudioUpload.java
  |   |   |	- YoutubeUpload.java
  |   |   |	- ExtractTags.java
  |   |   | - HeadersUtils.java	(utility file)
  |   | - test/
  | - target/
  | - pom.xml
```

Once you are done, go back to the root directory of your project, in this case:

```bash
cd samples/tagging/java/tagging
```

and then follow the commands below to run each file.

## Upload Audio File

[AudioUpload.java](AudioUpload.java)

Replace package name with your own project group ID, (in our case here: `com.example.tagging`)

```java
package com.example.tagging;
...
```

Required:  `API_KEY`

To run:

```bash
mvn exec:java -Dexec.mainClass="com.example.tagging.AudioUpload" -Dexec.args="audio file path here"
```

** **Note:** replace `com.example.tagging` with your own project group ID

## Upload Audio Link

[AudioLinkUpload.java](AudioLinkUpload.java)

Replace package name with your own project group ID, (in our case here: `com.example.tagging`)

```java
package com.example.tagging;
...
```

Required: `API_KEY`

To run:

```bash
mvn exec:java -Dexec.mainClass="com.example.tagging.AudioLinkUpload" -Dexec.args="audio link here"
```

** **Note:** replace `com.example.tagging` with your own project group ID

## Upload YouTube Link

[YouTubeUpload.java](YouTubeUpload.java)

Replace package name with your own project group ID, (in our case here: `com.example.tagging`)

```java
package com.example.tagging;
...
```

Required:  `API_KEY`

To run:

```bash
mvn exec:java -Dexec.mainClass="com.example.tagging.YoutubeUpload" -Dexec.args="Youtube link here"
```

** **Note:** replace `com.example.tagging` with your own project group ID

## Extract Tags

[ExtractTags.java](ExtractTags.java)

Replace package name with your own project group ID, (in our case here: `com.example.tagging`)

```java
package com.example.tagging;
...
```

Required:  `API_KEY`

To run:

```bash
mvn exec:java -Dexec.mainClass="com.example.tagging.ExtractTags" -Dexec.args="track ID here"
```

** **Note:** replace `com.example.tagging` with your own project group ID