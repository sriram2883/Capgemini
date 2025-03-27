using Microsoft.AspNetCore.Mvc;
using Microsoft.ApplicationInsights;
using Microsoft.ApplicationInsights.DataContracts;
using System;
using System.Collections.Generic;

[ApiController]
[Route("api/[controller]")]
public class TelemetryDemoController : ControllerBase
{
    private readonly TelemetryClient _telemetryClient;

    public TelemetryDemoController(TelemetryClient telemetryClient)
    {
        _telemetryClient = telemetryClient;
    }

    // VERBOSE TRACE
    [HttpGet("trace-verbose")]
    public IActionResult LogVerbose()
    {
        var message = "This is a VERBOSE log";
        var timestamp = DateTime.UtcNow;

        _telemetryClient.TrackTrace(message, SeverityLevel.Verbose);

        var logObject = new
        {
            message = message,
            severityLevel = "Verbose",
            timestamp = timestamp.ToString("o"),
            type = "Trace"
        };

        return Ok(logObject);
    }

    // INFORMATION TRACE
    [HttpGet("trace-info")]
    public IActionResult LogInfo()
    {
        var message = "This is an INFORMATION log";
        var timestamp = DateTime.UtcNow;

        _telemetryClient.TrackTrace(message, SeverityLevel.Information);

        var logObject = new
        {
            message = message,
            severityLevel = "Information",
            timestamp = timestamp.ToString("o"),
            type = "Trace"
        };

        return Ok(logObject);
    }

    // WARNING TRACE
    [HttpGet("trace-warning")]
    public IActionResult LogWarning()
    {
        var message = "This is a WARNING log";
        var timestamp = DateTime.UtcNow;

        _telemetryClient.TrackTrace(message, SeverityLevel.Warning);

        var logObject = new
        {
            message = message,
            severityLevel = "Warning",
            timestamp = timestamp.ToString("o"),
            type = "Trace"
        };

        return Ok(logObject);
    }

    // EXCEPTION
    [HttpGet("log-exception")]
    public IActionResult LogException()
    {
        string message = null;
        string type = null;
        string stackTrace = null;
        var timestamp = DateTime.UtcNow;

        try
        {
            int fail = 0;
            int result = 10 / fail;
        }
        catch (Exception ex)
        {
            message = ex.Message;
            type = ex.GetType().Name;
            stackTrace = ex.StackTrace;

            _telemetryClient.TrackException(ex);
        }

        var logObject = new
        {
            type = "Exception",
            exception = new
            {
                message = message,
                type = type,
                stackTrace = stackTrace
            },
            severityLevel = "Error",
            timestamp = timestamp.ToString("o")
        };

        return Ok(logObject);
    }

    // CUSTOM EVENT
    [HttpGet("log-event")]
    public IActionResult LogEvent()
    {
        var eventName = "UserSignedUp";
        var timestamp = DateTime.UtcNow;
        var properties = new Dictionary<string, string>
        {
            { "Plan", "Premium" },
            { "Region", "East US" }
        };

        _telemetryClient.TrackEvent(eventName, properties);

        var logObject = new
        {
            type = "Event",
            name = eventName,
            properties = properties,
            timestamp = timestamp.ToString("o")
        };

        return Ok(logObject);
    }

    // DEPENDENCY
    [HttpGet("log-dependency")]
    public IActionResult LogDependency()
    {
        var dependencyType = "SQL";
        var dependencyName = "GetUsers";
        var dependencyData = "SELECT * FROM Users";
        var timestamp = DateTimeOffset.UtcNow;
        var duration = TimeSpan.FromMilliseconds(200);
        var success = true;

        _telemetryClient.TrackDependency(
            dependencyType,
            dependencyName,
            dependencyData,
            timestamp,
            duration,
            success
        );

        var logObject = new
        {
            type = "Dependency",
            target = dependencyType,
            name = dependencyName,
            data = dependencyData,
            duration = duration.ToString(),
            success = success,
            timestamp = timestamp.ToString("o")
        };

        return Ok(logObject);
    }

    // REQUEST
    [HttpGet("log-request")]
    public IActionResult LogRequest()
    {
        var requestName = "HomePageRequest";
        var timestamp = DateTimeOffset.UtcNow;
        var duration = TimeSpan.FromMilliseconds(150);
        var responseCode = "200";
        var success = true;

        _telemetryClient.TrackRequest(
            requestName,
            timestamp,
            duration,
            responseCode,
            success
        );

        var logObject = new
        {
            type = "Request",
            name = requestName,
            duration = duration.ToString(),
            responseCode = responseCode,
            success = success,
            timestamp = timestamp.ToString("o")
        };

        return Ok(logObject);
    }
}
